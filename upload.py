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
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

w3 = w3storage.API(token=STORAGE_API_TOKEN)
web3 = Web3(Web3.HTTPProvider(IPC_URL))
isConnected = web3.isConnected()
print(isConnected)

#connect to smart contract


with open('contract_abi.json', 'r') as f:
  contract_abi = json.loads(f.read())

contract = web3.eth.contract(address=SMART_CONTRACT_ADDRESS, abi=contract_abi)

#to get time,date and place of a case
now = datetime.now()
current_time = str(now.strftime("%H:%M:%S"))
current_date = str(now.strftime("%d/%m/%Y"))
g = geocoder.ip('me')
geoLoc = Nominatim(user_agent="GetLoc")
camera_place = geoLoc.reverse(g.latlng)

location = geoLoc.geocode(camera_place)
longitude = str(location.longitude)
latitude = str(location.latitude)
camera_place = str(geoLoc.reverse(g.latlng))

#category of cases
category=["ROAD_ACCIDENT","HARRASMENT","ABDUCTION","PUBLIC_FIGHT"]

# def get_list():
#     return contract.functions.getCases().call()
# print(get_list())    

def doThingsWithNewFiles(newFiles: list,watchDirectory:str):
	for i in newFiles:
		video_cid = str(w3.post_upload((i, open(watchDirectory+"/"+i, 'rb'))))
		print(video_cid)
		os.remove(watchDirectory+"/"+i)
		# new_case = contract.functions.addCase
		# (video_cid,camera_place,current_time,current_date,category[0]
		# ).call()
		# print(new_case)
		transaction = contract.functions.addCase(
		video_cid,camera_place,current_time,current_date,category[0]
		).buildTransaction({
		'gas': 6000000,
		'gasPrice': web3.eth.gasPrice,
		'from': '0x24d4E35630e579b8E5807E469E487bf799A22B90',
		'nonce': web3.eth.getTransactionCount('0x24d4E35630e579b8E5807E469E487bf799A22B90')
		}) 
		print("new")
		print(web3.eth.gasPrice)
		print(transaction)
		print("new")
		
		private_key = PRIVATE_KEY 
		signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
		print(signed_txn)
		tx = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
		print(tx)
		
		  



def uploadNewFile(newFile:str):
	video_cid = w3.post_upload((newFile.split('/')[-1], open(newFile, 'rb')))
	print(video_cid)
	os.remove(newFile)
	# new_case = contract.functions.addCase
	# (video_cid,camera_place,current_time,current_date,category[0]
	# ).call()
	# print(new_case)
	transaction = contract.functions.addCase(
	video_cid,str(newFile),camera_place,longitude,latitude,current_time,current_date,category[0]
	).buildTransaction({
	'gas': 6000000,
	'gasPrice': web3.eth.gasPrice,
	'from': '0x24d4E35630e579b8E5807E469E487bf799A22B90',
	'nonce': web3.eth.getTransactionCount('0x24d4E35630e579b8E5807E469E487bf799A22B90')
	}) 
	print("new")
	print(web3.eth.gasPrice)
	print(transaction)
	print("new")
	
	private_key = PRIVATE_KEY 
	signed_txn = web3.eth.account.signTransaction(transaction, private_key=private_key)
	print(signed_txn)
	tx = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
	print(tx)
	