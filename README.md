# Elrond-NFT-mint-script
This repo explain one way of minting NFTs on Elrond with a python script. <br>

This was useful by the time collections were sold out fast, now this script is mainly a tool for curious people :)
Not yet finished though.

# Steps
There are several steps before launching the script. Namely, we need the smart contract address, its shard, the "minting" function name. <br>
To explain the steps better, I'll take the example of an arbitrary Elrond NFT mint : airkeys from Symbiosis.


## 1) Get the smart contract address

The smart contract address can be found prior to the public sale. Either the team has made a presale, or they probably minted the NFTs already (the buyers won't really mint the NFTs, only buy them, this is common on Elrond). In this case you can find the collection on the Explorer by checking the NFTs tab and look for the last NFTs issued/minted with a similar name. Be careful though with fake collections, the smart contract should have the adequate supply in it, and probably the owner already called several functions like whitelist if there is a presale. <br>

In our example, we find the collection AIRS-98b24d which corresponds to the Symbiosis airkeys collection, the smart contract has many whitelist transactions and the supply pre-mint is 3333. The smart contract address is `erd1qqqqqqqqqqqqqpgqpwlr5jtshg9pqf4txm5uvmykhpvzwvpgmxzqjqzcxz`


## 2) Prepare for the wallets 

Now that we have the smart contract address, we also know on which shard it was deployed. This is important as cross-shard transactions are slower, to be as fast as possible we want to have minting wallets on the same shard. You can create as many wallets you want [here](https://wallet.elrond.com/), the only constraint is the shard. <br>

Once you have the wallets you need to derive the pem file, the classical way of doing it is by using [erdpy](https://docs.elrond.com/sdk-and-tools/erdpy/deriving-the-wallet-pem-file/), but you can also check [Buildo Begins](https://github.com/ElrondDevGuild/buildo-begins) for an alternative way with TS. The pem file is required in order to make txs signing faster, however you should delete the files, and move your NFTs to your main wallet after the operation.

In our example the shard of the smart contract is 0 : 

<img width="1115" alt="image" src="https://user-images.githubusercontent.com/16515787/173248005-44387481-b30d-4d3c-9ddb-0830ed1eda72.png">


## 3) Minting/buying function name

In order to find the smart contract's minting/buying function name you can convert the smart contract's bytecode to text using for example [this converter](http://www.unit-conversion.info/texttools/hexadecimal/).

The bytecode can be found in the code tab : 

<img width="1115" alt="image" src="https://user-images.githubusercontent.com/16515787/173248081-8031d148-e8d4-45e5-9d88-bcdad589eeb9.png">

Copy-pasting the code in the converter, we have can find a list of function names in the output : 

<img width="937" alt="image" src="https://user-images.githubusercontent.com/16515787/173248120-35c8f25a-fcdc-452d-ac03-0f346869c151.png">

There are several functions, the one that is interesting for us should have "mint" or "buy" in the name. In our example the function name is "buy", and for the presale it is "buyPresale".


## 4) Executing the script

We now have :

<ul>
  <li> The address of the smart contract </li>
  <li> The function name to mint NFTs </li>
  <li> One or several wallets on the same shard than the SC, ready to mint (all the pem file should be in the same folder) </li>
</ul>  

Now you can execute the python script with the following command : 

```python3 mint.py --sc_address THE_SMART_CONTRAT_ADDRESS --function THE_FUNCTION_NAME --price THE_PRICE_FOR_1_NFT --quantity THE_QUANTITY_OF_NFT_YOU_WANT_PER_WALLET --pem THE_FOLDER_OF_ALL_YOUR_PEM_FILES`
