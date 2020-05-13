#!/usr/bin/env python3
import csv
import sys

from lib.cta_exception import cta_exception_handler

def cta_writer_init(jsonOutput):
    try:
        #print("test")
        print(', '.join(jsonOutput))
        return
    
    except Exception as exceptValue:
        cta_exception_handler(exceptValue, __name__)
        return


if __name__=="__main__":
    jsonOutput = "DebuggingString"
    cta_writer_init(jsonOutput)