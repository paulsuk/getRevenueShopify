import urllib.request as request

API_BASE_URL = "https://shopicruit.myshopify.com/admin/orders.json?page="
ACCESS_TOKEN = "c32313df0d0ef512ca64d5b336a0d7c6"

def get_data(pageNumber):
	url = API_BASE_URL + "%d&access_token=" % pageNumber + ACCESS_TOKEN 
	req = request.Request(url)
	with request.urlopen(req) as response:
		the_page = response.read()
	print(the_page)

if __name__ == '__main__':
	get_data(5)