import json
from web3 import Web3
import w3storage

infura_url = 'https://polygon-mumbai.g.alchemy.com/v2/4DMdz2O8T580302fMXkvfoIvP2AZ2hea'
web3 = Web3(Web3.HTTPProvider(infura_url))

isConnected = web3.isConnected()
print(isConnected)
blocknumber = web3.eth.blockNumber

balance = web3.eth.getBalance('0x24d4E35630e579b8E5807E469E487bf799A22B90')

