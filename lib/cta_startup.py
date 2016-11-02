#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import configparser
import sys

from lib.cta_exception import cta_exception_handler

# Parses arguements.
def cta_argument_parser():
    exceptFunction = "cta_argument_parser"
    try:
        parser = argparse.ArgumentParser(description="""
Cybert Threat Aggregator
cta.py takes as input a text file of hashes or strings,  or a single 
hash value or string and performs a searh of various sources.  The purpose of 
this application is to identify of the strings are known by threat intelligence
sources.  The application will output to the stdout all findings in CSV format.

Example 1:  cta.py -s 0d1ef429ed4a31753e5905e5356ba94d
Example 2:  cta.py -s kernel32.dll
Example 3:  cta.py -s File-Of-Strings.txt

It may also be beneficial to redirect the stdout to to a csv file like in the 
example below.

Example 4:  cta.py -s kernel32.dll > out.csv

https://github.com/aubsec/cta.git
https://twitter.com/aubsec
https://aubsec.github.io""", formatter_class=RawTextHelpFormatter)
        parser.add_argument("-s", "--string", help="""
Required. Specify a single hash value, string, or file of strings to 
search.""", required=True)
        parser.add_argument("-c", "--config", help="Specify Config File.", default="cta_config.conf", required=False)
        args = parser.parse_args()
# These are here for debugging purposes.
        sys.stderr.write("[+] String being parsed: " + str(args.string) + "\n")
        return(args)

    except Exception as exceptValue:
        return(exceptValue, exceptFunction)

# Goal is to parse a configuration file
# Currently is not working right. 
def cta_config(args):
    exceptFunction = "cta_argument_parser"
    try:
#        with open(args.config, "r") as configFile:
#            for line in configFile:
#                sys.stderr.write(line + "\n")
        config = configparser.ConfigParser()

        config.read(args.config)
        
        for i in config.sections():
            print(config.sections)

    
    except Exception as exceptValue:
        cta_exception_handler(exceptValue, exceptFunction)




def cta_init(args):
    exceptFunction = "cta_init()"
    try:
        with open(args.string) as fileName:
            for line in fileName:
                sys.stderr.write(line)
        return

    except:
        print(args.string)
        return