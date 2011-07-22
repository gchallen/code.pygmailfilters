#!/usr/bin/env python

import sys
import GmailFilters

input = open(sys.argv[1])
filters = GmailFilters.GmailFilters(input.read())
print filters[0].getProperty("from")[0].get("value")
filters[0].newProperty("to", "me@me.com")
print filters
