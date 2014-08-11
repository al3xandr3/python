#!/usr/bin/python

from __future__ import with_statement
import sys, string, xmlrpclib, re, os

if len(sys.argv) < 8:
	print("Use: python confluence.py spacekey pagetitle contentType filename username password server")
	sys.exit("Eg.: python confluence.py '~page' 'sandbox' 'application/pdf' file.pdf 'user' 'pass' 'your.domain.com' ")


spacekey = sys.argv[1]
pagetitle = sys.argv[2]
contentType = sys.argv[3]
filename = sys.argv[4]
username = sys.argv[5]
password = sys.argv[6]
server = sys.argv[7]

#read data
with open(filename, 'rb') as f:
    data = f.read()

#server = xmlrpclib.ServerProxy('https://user:pass@your.domain.com/rpc/xmlrpc')
server = xmlrpclib.ServerProxy('https://%s:%s@%s' % (username, password, server) + "/rpc/xmlrpc")
token = server.confluence1.login(username, password)
page = server.confluence1.getPage(token, spacekey, pagetitle)
if page is None:
    exit("Could not find page " + spacekey + ":" + pagetitle)

attachment = {}
attachment['fileName'] = os.path.basename(filename)
attachment['contentType'] = contentType

server.confluence1.addAttachment(token, page['id'], attachment, xmlrpclib.Binary(data))
