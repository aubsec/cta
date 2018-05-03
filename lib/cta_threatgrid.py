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
#    sys.stderr.write("[!] Testing!\n")
    try:

        #searchString = searchString.replace("\n","")
        count = 0
        builtQuery = (URL + "api_key=" + apiKey + "&q=" + searchString)
        #sys.stderr.write(builtQuery + "\n")
        responseQuery = urllib.request.urlopen(builtQuery).read()
        jsonResponse = json.loads(responseQuery.decode('utf-8'))
# The following two lines are for debugging. 
        #sys.stderr.write(__name__ + "\n")
        #sys.stderr.write(json.dumps(jsonResponse, sort_keys=True, indent=4))

        if jsonResponse["data"]["total"] != 0:
            print("ThreatGrid Search: " + searchString)
            print("Permalink: https://panacea.threatgrid.com/mask/#/search/samples?q=" 
            + searchString + "&term=freeform&_k=b80gmg")
            for item in jsonResponse["data"]["items"]:
                print("Filename: " + str(item["item"]["filename"]))
                print("Submitted At: " + str(item["item"]["submitted_at"]))
                print("SHA256 Hash: " + str(item["item"]["sha256"]))
                print("Threat Score: " + str(item["item"]["analysis"]["threat_score"]))
                print()
                count += 1
                if count == 5:
                    break
                else:
                    continue
        #else:
        #   sys.stderr.write("[*] " + searchString + " not found.\n")            
        return
    except Exception as exceptValue:
        cta_exception_handler(exceptValue, __name__)
        return


if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_threatgrid_init(searchString, apiKey)