#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import configparser
import sys
from lib.cta_exception import cta_exception_handler

# Souce Imports.  Add new sources to the following list. 
from lib.cta_threatgrid import cta_threatgrid_init
from lib.cta_virustotal import cta_virustotal_init


# Parses arguements.
def cta_argument_parser():

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
        parser.add_argument("-c", "--config", help="Specify Config File.", 
            default="cta_config.conf", required=False)
        args = parser.parse_args()
# These are here for debugging purposes.
        sys.stderr.write("[+] String being parsed: " + str(args.string) + "\n")
        return(args)

    except Exception as exceptValue:
        cta_exception_handler(exceptValue, __name__)

# Goal is to parse a configuration file
# Currently is not working right. 
def cta_config(searchString, args):

    try:
        config = configparser.ConfigParser()
        config.read(args.config)
# For every section in the config file, test if it is Enabled, if so call it's
# respective function. 
# To add new functionalitiy, modify the config file, add the new class to the
# /lib/ folder, and add the appropriate import to the top.
        for section in config.sections():
# Verifies that the section is enabled. 
            if config[section]["Enabled"] == "True":
                apiKey = config[section]["API"]
# These following statements build the name of the method being called based
# on the name of the section in the configuration file. 
                methodName = eval(("cta_" + section + "_init").lower())
                methodName(searchString, apiKey)
            else:
                continue
        return
                
    except Exception as exceptValue:
        cta_exception_handler(exceptValue, __name__)

# Simple method that is called by cta.py to begin execution of the program.
def cta_init(args):
    try:
        with open(args.string) as fileName:
            for searchString in fileName:
                #sys.stderr.write(line)
                cta_config(searchString, args)
        return

    except:
        searchString = args.string
        cta_config(searchString, args)
        return

if __name__=="__main__":
    sys.stderr.write("[!] Please execute program from cta.py.\n")
    exit(0)