#!/usr/bin/env python3
import urllib.request
import json
import sys

try:
    from lib.cta_exception import cta_exception_handler
except:
    pass

URL = "https://investigate.api.umbrella.com/score/"

def cta_umbrella_init(searchString, apiKey):
    try:
        headers = {
        'Authorization': 'Bearer ' + apiKey
        }

        builtQuery = (URL + searchString)
        #sys.stderr.write(builtQuery + "\n")
        requestQuery = urllib.request.Request(builtQuery, headers=headers)
        responseQuery = urllib.request.urlopen(requestQuery).read()
        print("Umbrella Score: " + responseQuery)

        return

    except Exception as exceptValue:
        cta_exception_handler(exceptValue, __name__)
    return

if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_umbrella_init(searchString, apiKey)