from erdpy.accounts import Account
from erdpy.proxy import ElrondProxy
from erdpy.transactions import Transaction

import argparse
import glob



# ---------------------------------------------------------------- #
#                         INPUTS
# ---------------------------------------------------------------- #
parser = argparse.ArgumentParser()
parser.add_argument("--sc_address", help="The smart contract address", required=True)
parser.add_argument("--function", help="The function name to mint", required=True)
parser.add_argument("--price", help="The price of 1 NFT", required=True)
parser.add_argument("--quantity", help="The quantity of NFT per wallet desired", required=True)
parser.add_argument("--pem", help="The pem folder", required=True)


args = parser.parse_args()

sc_address = args.sc_address
function_name = args.function
price_per_NFT = args.price
quantity_per_wallet = args.quantity
pem_dir = args.pem


# ---------------------------------------------------------------- #
#                         CONSTANT
# ---------------------------------------------------------------- #
EGLD_DECIMALS = 10**18


# ---------------------------------------------------------------- #
#                         HELPER FUNCTIONs
# ---------------------------------------------------------------- #
def int_to_BigUint(num) : 
    return int(f"{num*EGLD_DECIMALS:.1f}".split(".")[0])         

# Sometimes need to add a 0 (if it's even, to be sure that is grouped by bytes)
def num_to_hex(num) : 
    hexa = format(num, "x")
    if len(hexa)%2==1 :  
        return "0" + hexa
    return hexa


# ---------------------------------------------------------------- #
#                   MAIN BUYING FONCTION
# ---------------------------------------------------------------- #
def buyNFTs(user) :

    tx = Transaction()
    tx.nonce = user.nonce
    tx.value = int_to_BigUint(price_per_NFT*quantity_per_wallet)
    tx.sender = user.address.bech32()
    tx.receiver = sc_address
    tx.gasPrice = gas_price
    tx.gasLimit = 250000000
    tx.data = function_name + "@" + num_to_hex(quantity_per_wallet)
    tx.chainID = chain
    tx.version = tx_version

    tx.sign(user)
    tx.send(proxy)

    user.nonce += 1  


# ---------------------------------------------------------------- #
#                  SETTING MAINNET PARAMS
# ---------------------------------------------------------------- #
proxy = ElrondProxy("https://gateway.elrond.com")
network = proxy.get_network_config()
chain = network.chain_id
gas_price = network.min_gas_price
tx_version = network.min_tx_version


for pem in glob.glob(pem_dir+"/*.pem") : 
    user = Account(pem_file=pem)
    user.sync_nonce(proxy)
    buyNFTs(user)

