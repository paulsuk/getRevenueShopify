import json
import pdb
import urllib.request as request

API_BASE_URL = "https://shopicruit.myshopify.com/admin/orders.json?page="
ACCESS_TOKEN = "c32313df0d0ef512ca64d5b336a0d7c6"

def get_data():
	''' 
	Method that will make calls to the API to get the sale information, iterating through the pages until there are no more pages
	The data will be held in SOME OBJECT and returned
	'''
	pageNumber = 1 # Using pageNumber 1 as default for now

	url = API_BASE_URL + "%d&access_token=" % pageNumber + ACCESS_TOKEN 
	req = request.Request(url)
	with request.urlopen(req) as response:
		pdb.set_trace()
		response_string = response.read().decode('utf-8')
		data = json.loads(response_string)
		

if __name__ == '__main__':
	get_data()