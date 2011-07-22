#!/usr/bin/env python

import sys
import GmailFilters

input = open(sys.argv[1])
filters = GmailFilters.GmailFilters(input.read())

allproperties = {}
for filter in filters:
  for key in filter.properties.keys():
    if not allproperties.has_key(key):
      allproperties[key] = set([])
    allproperties[key].add(filter.properties[key])

print allproperties.keys()
