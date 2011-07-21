#!/usr/bin/env python

import sys,urllib2
from BeautifulSoup import BeautifulSoup

input = open(sys.argv[1])
soup = BeautifulSoup(input.read())
print soup.prettify()
