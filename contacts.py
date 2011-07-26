#!/usr/bin/env python

import atom
import gdata.contacts.data
import gdata.contacts.client
import getpass

username = raw_input("Username: ")
password = getpass.getpass("Password: ")

client = gdata.contacts.client.ContactsClient()
client.ClientLogin(username, password, client.source)

feed = client.GetContacts()
while True:
  for entry in feed.entry:
    print entry.title.text
  uri = feed.GetNextLink()
  if uri == None:
    break
  feed = client.get_feed(uri=uri.href)
