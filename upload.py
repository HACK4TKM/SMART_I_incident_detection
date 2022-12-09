import json
from web3 import Web3
import w3storage
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim

 
infura_url = 'https://polygon-mumbai.g.alchemy.com/v2/4DMdz2O8T580302fMXkvfoIvP2AZ2hea'
web3 = Web3(Web3.HTTPProvider(infura_url))

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d/%m/%Y")
g = geocoder.ip('me')
geoLoc = Nominatim(user_agent="GetLoc")
locname = geoLoc.reverse(g.latlng)



isConnected = web3.isConnected()
print(isConnected)
blocknumber = web3.eth.blockNumber
balance = web3.eth.getBalance('0x24d4E35630e579b8E5807E469E487bf799A22B90')


