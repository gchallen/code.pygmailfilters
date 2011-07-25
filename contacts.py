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
