#!/usr/bin/env python3
import urllib.request
import json
import sys

try:
	from lib.cta_exception import cta_exception_handler
except:
	pass

# API = 
URL = "https://panacea.threatgrid.com/api/v2/search/submissions?"

def cta_threatgrid_init(searchString, apiKey):
	jsonResponse = dict()
	try:
		builtQuery = (URL + "api_key=" + apiKey + "&q=" + searchString)
		responseQuery = urllib.request.urlopen(builtQuery).read()
		jsonResponse = json.loads(responseQuery.decode('utf-8'))
		sys.stderr.write(__name__ + "\n")
		print(jsonResponse)
		return
	except Exception as exceptValue:
		cta_exception_handler(exceptValue, __name__)


if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_threatgrid_init(searchString, apiKey)