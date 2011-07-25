#!/usr/bin/env python

import sys
import GmailFilters

input = open(sys.argv[1])
filters = GmailFilters.GmailFilters(input.read())
print filters[0].From
print filters[0].ShouldMarkAsRead
filters[0].ShouldMarkAsRead = False
del(filters[0].ShouldMarkAsRead)
print filters
