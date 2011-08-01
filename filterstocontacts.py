#!/usr/bin/env python

import sys,re
import GmailFilters
import lepl.apps.rfc3696
import atom
import gdata.contacts.data
import gdata.contacts.client
import getpass

input = open(sys.argv[1])
filters = GmailFilters.GmailFilters(input.read())
emailValidator = lepl.apps.rfc3696.Email()
orderedLabelPattern = re.compile(r'\(\d+\)\s+(\w+)')

emailsToGroups = {}

for f in filters:
  if f.From == None or f.Label == None:
    continue
  if not emailValidator(f.From):
    continue
  
  orderedLabelMatch = orderedLabelPattern.match(f.Label)
  if orderedLabelMatch != None:
    label = orderedLabelMatch.group(1)
  else:
    label = f.Label
  emailsToGroups[f.From] = "Filter to %s" % (label)

username = raw_input("Username: ")
password = getpass.getpass("Password: ")

client = gdata.contacts.client.ContactsClient()
client.ClientLogin(username, password, client.source)

groupNamesToAtomIDs = {}

feed = client.GetGroups()
while True:
  for entry in feed.entry:
    groupNamesToAtomIDs[entry.title.text] = entry.id.text
  uri = feed.GetNextLink()
  if uri == None:
    break
  feed = client.get_feed(uri=uri.href)

contactEmailsToAtomIDs = {}
feed = client.GetContacts()
#while True:
for i in range(5):
  for entry in feed.entry:
    print i
    if not hasattr(entry, 'email'):
      print "Fuck"
      continue
    for email in entry.email:
      contactEmailsToAtomIDs[email.address] = entry.id.text
  uri = feed.GetNextLink()
  print uri
  if uri == None:
    break
  feed = client.GetContacts(uri=uri.href)
