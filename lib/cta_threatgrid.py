#!/usr/bin/env python3

from lib.cta_exception import cta_exception_handler

# Debugging Constants
# API = 




def cta_threatgrid_init(searchString, apiKey):

	try:
		print(__name__, searchString, apiKey)
		return

	except Exception as exceptValue:
		cta_exception_hander(exceptValue, __name__)



if __name__=="__main__":
    apiKey = API
    searchString = "DebuggingString"
    cta_threatgrid_init(searchString, apiKey)