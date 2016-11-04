#!/usr/bin/env python3
import urllib.request
import json
import sys

try:
	from lib.cta_exception import cta_exception_handler
except:
	pass

# API = 
URL = "https://www.virustotal.com/vtapi/v2/file/report?"

def cta_virustotal_init(searchString, apiKey):
	jsonResponse = dict()
	try:
		builtQuery = (URL + "apikey=" + apiKey + "&resource=" + searchString)
		sys.stdout.write(builtQuery)
		try:
			responseQuery = urllib.request.urlopen(builtQuery)
			responseEncoding = responseQuery.info().get_content_charset('utf-8')
			jsonResponse = json.loads(data.decode(responseEncoding))
			print(jsonResponse)
		except:
			sys.stderr.write("[!] Unable to complete VirusTotal API request.\n")
		return
	except Exception as exceptValue:
		cta_exception_hander(exceptValue, __name__)


if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_virustotal_init(searchString, apiKey)