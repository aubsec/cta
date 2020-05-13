#!/usr/bin/env python3
import urllib.request
import json
import ssl
import sys

try:
    from lib.cta_exception import cta_exception_handler
    from lib.cta_writer import cta_writer_init
except:
    pass

# API = 
URL = "https://panacea.threatgrid.com/api/v2/search/submissions?"
ssl._create_default_https_context = ssl._create_unverified_context

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
            jsonOutput = []
            jsonOutput.append(searchString)
            jsonOutput.append(str("https://panacea.threatgrid.com/mask/#/search/samples?q=" 
            + searchString + "&term=freeform&_k=b80gmg"))
            for item in jsonResponse["data"]["items"]:
                jsonOutput.append(str(item["item"]["filename"]))
                jsonOutput.append(str(item["item"]["submitted_at"]))
                jsonOutput.append(str(item["item"]["sha256"]))
                jsonOutput.append(str(item["item"]["analysis"]["threat_score"]) + ",,")
                cta_writer_init(jsonOutput)
                count += 1
                if count == 1:
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