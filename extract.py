#!/usr/bin/env python

import sys
from lib import GmailFilters

input = open(sys.argv[1])
print GmailFilters(input.read())
