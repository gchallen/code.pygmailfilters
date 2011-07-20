#!/usr/bin/env python

import sys,re,urllib2
from BeautifulSoup import BeautifulSoup
from lib import GMailFilter

input = open(sys.argv[1])
soup = BeautifulSoup(input.read())
filters = GMailFilter.fromSoup(soup)
