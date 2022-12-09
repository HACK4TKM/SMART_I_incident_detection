import json
from web3 import Web3
import w3storage
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim

 
infura_url = 'https://polygon-mumbai.g.alchemy.com/v2/4DMdz2O8T580302fMXkvfoIvP2AZ2hea'
web3 = Web3(Web3.HTTPProvider(infura_url))
smart_contract_address = '0xDBCE74954eE89De555250678e3f3B3906B8DB3B0'
with open('contract_abi.json', 'r') as f:
  contract_abi = json.loads(f.read())


#to get time,date and place of a case
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d/%m/%Y")
g = geocoder.ip('me')
geoLoc = Nominatim(user_agent="GetLoc")
locname = geoLoc.reverse(g.latlng)
#category of cases
category=["ROAD_ACCIDENT","HARRASMENT","ABDUCTION","PUBLIC_FIGHT"]

isConnected = web3.isConnected()
print(isConnected)
blocknumber = web3.eth.blockNumber
balance = web3.eth.getBalance('0x24d4E35630e579b8E5807E469E487bf799A22B90')


contract = web3.eth.contract(address=smart_contract_address, abi=contract_abi)
print(contract)