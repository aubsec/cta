#!/usr/bin/env python3
import sys

# Collects error codes and prints to screen
def cta_exception_handler(exceptValue, exceptFunction):
    sys.stderr.write("[!] An exception has occured in " + str(exceptFunction) + "\n")
    sys.stderr.write("[!] " + str(exceptValue) + "\n")
    exit(1)