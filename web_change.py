
# TODO
## How to keep the history ?

import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import time
import requests
import sys
import livemail as mail


def url_change_check(url, toaddrs, subj, msg, server, port, username, password):

	response = requests.get(url)

	# retry:
	if not response.ok:
		response = requests.get(url)

	if not response.ok:
		response = requests.get(url)
	    
	import hashlib
	new = hashlib.md5(response.content).hexdigest()

	fhash = os.path.expanduser("res.txt")

	# get previous
	prev=""
	if os.path.isfile(fhash):
		prev = open(fhash, "rb").read()

	# compare, email is different
	if new != prev:
		mail.mail(toaddrs, subj, msg, server, port, username, password)

		# save new
		file = open(fhash, "w")
		file.write(new)
		file.close()




# https://developer.yahoo.com/yql/

# scrap any page: http://selectorgadget.com/ -> find css_selector
# YQL: "SELECT * FROM data.html.cssselect WHERE url='http://finance.yahoo.com/q?s=MSFT' AND css='#yfs_l84_msft'"
def getYQL (query):

	import urllib
	url = "http://query.yahooapis.com/v1/public/yql?q="
	url += urllib.quote(query)
	url += "&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

	response = requests.get(url)

	# retry:
	if not response.ok:
		response = requests.get(url)

	if not response.ok:
		response = requests.get(url)

	yqlxml = response.content
	from bs4 import BeautifulSoup

	#If error print
	soup = BeautifulSoup(yqlxml, "xml")
	res = soup.select("error")
	if res:
		raise Exception(res[0].string)

	###############
	# Get the xml
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(yqlxml, "xml")
	res = soup.select("results")[0].string


	return res

if __name__ == "__main__":

	print "Please use as a lib"

	#print getYQL("SELECT * FROM data.html.cssselect WHERE url='http://finance.yahoo.com/q?s=MSFT' AND css='#yfs_l84_msft'")

	#print getYQL("SELECT * FROM data.html.cssselect WHERE url='http://www.aliexpress.com/w/wholesale-joyo-california.html?site=glo&SortType=price_asc&shipCountry=ee&SearchText=joyo+california&CatId=100005416' AND css='.list-item-first .value'")

	#print getYQL("SELECT * FROM data.html.cssselect WHERE url='http://www.aliexpress.com/wholesale?shipCountry=ee&shipCompanies=&SearchText=caline+pure+sky&exception=&minPrice=&maxPrice=&minQuantity=&maxQuantity=&isFreeShip=y&isFavorite=n&isRtl=n&isOnSale=n&isAtmOnline=n&isBigSale=n&similar_style=n&similar_style_id=&CatId=0&SortType=price_asc&initiative_id=AS_20141122025247&filterCat=100005416&groupsort=1' AND css='.list-item-first .value'")

	# Get USD - EUR rate
	#print getYQL("SELECT * FROM data.html.cssselect WHERE url='http://www.msn.com/en-us/money/tools/currencyconverter/fi-USD-EUR' AND css='#frmrate'")

