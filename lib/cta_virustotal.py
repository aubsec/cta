#!/usr/bin/env python3
import urllib.request
import json
import sys
import time

try:
	from lib.cta_exception import cta_exception_handler
except:
	pass

# API = 
URL = "https://www.virustotal.com/vtapi/v2/file/report?"

def cta_virustotal_init(searchString, apiKey):
	jsonResponse = dict()
	try:
		sys.stderr.write("[*] Waiting 15 seconds for VirusTotal. \n")
		time.sleep(15)
		builtQuery = (URL + "apikey=" + apiKey + "&resource=" + searchString)
		responseQuery = urllib.request.urlopen(builtQuery).read()
		jsonResponse = json.loads(responseQuery.decode("utf-8"))

		print("\nVirusTotal Search")
		print("Permalink: " + jsonResponse["permalink"])
		print("SHA256 Hash: " + jsonResponse["sha256"])
		print("Detection Ratio: " 
			+ str(jsonResponse["positives"]) 
			+ "/" 
			+ str(jsonResponse["total"]))
		return
	except Exception as exceptValue:
		cta_exception_handler(exceptValue, __name__)
		return


if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_virustotal_init(searchString, apiKey)