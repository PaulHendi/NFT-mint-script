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

## 3) Minting/buying function name


