import decimal
import json
import pdb
import urllib.request as request

class MoneyCounter(object):
	API_BASE_URL = 'https://shopicruit.myshopify.com/admin/orders.json?page='
	ACCESS_TOKEN = 'c32313df0d0ef512ca64d5b336a0d7c6'

	class OrderDetails(object):
		# Class will hold all relevant data for a single order, created using the response from API

		def __init__(self, order):
			# We can easily add more fields, but only adding id and price unless something else comes up that I need
			self.id = order['id']
			# Will only use the USD price for the sake of consistency. I am also using decimal to represent prices to avoid floating point error from floats/doubles
			self.price = decimal.Decimal(order['total_price_usd'])

	def _get_data(self):

		''' 
		Method that will make calls to the API to get the sale information, iterating through the pages until there are no more pages
		Each order is stored by OrderDetails and this method will return a list of OrderDetails
		'''
		orders = []
		pageNumber = 1 # Using pageNumber 1 as default for now

		response = self._api_call(pageNumber)
		while response:
			print(pageNumber)
			for order in response:
				orderDetails = self.OrderDetails(order) 
				orders.append(orderDetails)

			pageNumber += 1
			response = self._api_call(pageNumber)

		return orders

	def _api_call(self, pageNumber):
		# Method for calling on the API
		url = self.API_BASE_URL + '%d&access_token=' % pageNumber + self.ACCESS_TOKEN 
		req = request.Request(url)
		orders = []

		with request.urlopen(req) as response:
			#pdb.set_trace()
			response_json = json.loads(response.read().decode('utf-8'))
			orders = response_json['orders']
		return orders

	def countMoney(self):
		orders = self._get_data()
		# Now need to go through the orders to sum up the prices, save and return it	

	def __init__(self):
		# Set precision for decimal to be 2. 
		decimal.getcontext().prec = 2

if __name__ == '__main__':
	moneyCounter = MoneyCounter()	
	moneyCounter.countMoney()