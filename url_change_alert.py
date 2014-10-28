
import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import time
import requests
import sys
import livemail as mail

def url_change_alert (url, toaddrs, subj, msg, server, port, username, password):

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


if __name__ == "__main__":

	print "Use as a lib!"

