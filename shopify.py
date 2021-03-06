import decimal
import json
import pdb
import urllib.request as request

class MoneyCounter(object):
	API_BASE_URL = 'https://shopicruit.myshopify.com/admin/orders.json?page='
	ACCESS_TOKEN = 'c32313df0d0ef512ca64d5b336a0d7c6'
	totalRevenue = 0
	numOrders = 0
	orders = []


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
		pageNumber = 1

		response = self._api_call(pageNumber)
		while response:
			for order in response:
				orderDetails = self.OrderDetails(order) 
				orders.append(orderDetails)

			pageNumber += 1
			response = self._api_call(pageNumber)

		self.orders = orders
		return orders

	def _api_call(self, pageNumber):
		# Method for calling on the API
		url = self.API_BASE_URL + '%d&access_token=' % pageNumber + self.ACCESS_TOKEN 
		req = request.Request(url)
		orders_json = []

		with request.urlopen(req) as response:
			response_json = json.loads(response.read().decode('utf-8'))
			orders_json = response_json['orders']
		return orders_json

	def countMoney(self):
		# Takes the orders and 
		orders = self._get_data()
		revenue = 0
		for order in orders:
			revenue += order.price
			print(revenue)

		self.totalRevenue = revenue
		self.numOrders = len(orders)
		
	def __init__(self):
		# Set precision for decimal to be 2. 
		decimal.getcontext().prec = 9
		self.countMoney()
		print("The total revenue is ${0:.2f} from {1} orders".format(self.totalRevenue, self.numOrders))

if __name__ == '__main__':
	moneyCounter = MoneyCounter()
