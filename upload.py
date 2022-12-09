import json
from dotenv import load_dotenv
load_dotenv()
import os
from web3 import Web3
import w3storage
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim


IPC_URL = os.getenv('IPC_URL')
SMART_CONTRACT_ADDRESS = os.getenv('SMART_CONTRACT_ADDRESS')
STORAGE_API_TOKEN = os.getenv('STORAGE_API_TOKEN')

w3 = w3storage.API(token=STORAGE_API_TOKEN)
web3 = Web3(Web3.HTTPProvider(IPC_URL))
isConnected = web3.isConnected()
print(isConnected)

#connect to smart contract
smart_contract_address = SMART_CONTRACT_ADDRESS

with open('contract_abi.json', 'r') as f:
  contract_abi = json.loads(f.read())

contract = web3.eth.contract(address=smart_contract_address, abi=contract_abi)

#to get time,date and place of a case
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d/%m/%Y")
g = geocoder.ip('me')
geoLoc = Nominatim(user_agent="GetLoc")
locname = geoLoc.reverse(g.latlng)

#category of cases
category=["ROAD_ACCIDENT","HARRASMENT","ABDUCTION","PUBLIC_FIGHT"]

# def get_list():
#     return contract.functions.getCases().call()
# print(get_list())    

def doThingsWithNewFiles(newFiles: list,watchDirectory:str):
    for i in newFiles:
        video_cid = w3.post_upload((i, open(watchDirectory+"/"+i, 'rb')))
        print(video_cid)


