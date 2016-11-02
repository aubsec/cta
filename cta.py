#!/usr/bin/env python3

# cta.py is used to search mostly open-source resousrces for suspicious 
# strings.  The goal being that allow a single point for searching many 
# sources and providing the output in CSV format.
#
# Copyright (C) 2016 Matthew Aubert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# https://github.com/aubsec/cta.git
# https://twitter.com/aubsec
# https://aubsec.github.io
import datetime
#import hashlib
#import os
import sys
#import tempfile
#import urllib.request
#import zipfile

from lib.cta_startup import cta_argument_parser, cta_config, cta_init
from lib.cta_exception import cta_exception_handler


def cta_main():
# Sets default exception values.
    exceptFunction = "main()"
    exceptValue = None
# Executes primary purpose of application.
    try:
        args = cta_argument_parser()
        cta_init(args)
        exceptFunction = cta_config(args)
# Instantiates object based on class NSRLDownload() and calls method GetNSRL().
#        nsrl = NsrlLookup()
#        
#        exceptValue,exceptFunction = nsrl.getNsrl()
# If program completed sucessfully, write sucess message to stderr and exit with 0.
        sys.stderr.write("[+] Program completed sucessfully.\n")
        exit(0)
# If execution fails, collects errors and passes them to the ExeceptionHandler() function.
    except Exception as exceptValue:
        cta_exception_handler(exceptValue, exceptFunction)

if __name__=="__main__":
    cta_main()
