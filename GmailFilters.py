import sys
from lxml import etree
from StringIO import StringIO

ATOM_NAMESPACE = "http://www.w3.org/2005/Atom"
APPS_NAMESPACE = "http://schemas.google.com/apps/2006"
ATOM = "{%s}" % ATOM_NAMESPACE
APPS = "{%s}" % APPS_NAMESPACE

NSMAP = {None : ATOM_NAMESPACE,
         "apps" : APPS_NAMESPACE}

namespaces = {'atom' : 'http://www.w3.org/2005/Atom',
              'apps' : 'http://schemas.google.com/apps/2006'}

class GmailFilters:

  # 21 Jul 2011 : GWA : Support loading from a pre-exported filter set or from scratch.

  def __init__(self, string):
    if string == "":
      self.feed = etree.Element(ATOM + "feed", nsmap=NSMAP)
      etree.SubElement(self.feed, ATOM + "title")
      etree.SubElement(self.feed, ATOM + "id")
      etree.SubElement(self.feed, ATOM + "updated")
      author = etree.SubElement(self.feed, ATOM + "author")
      etree.SubElement(author, ATOM + "name")
      etree.SubElement(author, ATOM + "email")
      self.setAuthor("", "")
    else:
      f = StringIO(string)
      self.tree = etree.parse(f)
      self.feed = self.tree.xpath('/atom:feed', namespaces=namespaces)[0]

    self.setTitle("Mail Filters")
    self.setID("")
    self.setUpdated("")

  def setTitle(self, text):
    title = self.feed.xpath('/atom:feed/atom:title', namespaces=namespaces)[0]
    title.text = text
  
  def setID(self, text):
    id = self.feed.xpath('/atom:feed/atom:id', namespaces=namespaces)[0]
    id.text = text
  
  def setUpdated(self, text):
    updated = self.feed.xpath('/atom:feed/atom:updated', namespaces=namespaces)[0]
    updated.text = text

  def setAuthor(self, name, email):
    nameelement = self.feed.xpath('/atom:feed/atom:author/atom:name', namespaces=namespaces)[0]
    nameelement.text = name
    emailelement = self.feed.xpath('/atom:feed/atom:author/atom:email', namespaces=namespaces)[0]
    emailelement.text = email

  def __getitem__(self, key):
    return GmailFilter(self.feed.xpath('/atom:feed/atom:entry', namespaces=namespaces)[key])

  def __repr__(self):
    return etree.tostring(self.feed, xml_declaration=True, encoding="utf-8", pretty_print=True)

class GmailFilter:

  # 22 Jul 2011 : GWA : These seem to be the defined actions at least based on what I can see.

  actions = ["label", "shouldTrash", "shouldNeverMarkAsImportant", "label", "shouldMarkAsRead", "shouldArchive", "forwardTo"]

  searches = ["from", "to", "subject", "hasTheWord"]

  # 22 Jul 2011 : GWA : Support loading from a pre-exported filter or from scratch.
  
  def __init__(self, entry):
    if entry == None:
      self.entry = etree.Element(ATOM + "entry")
      etree.SubElement(self.entry, ATOM + "category")
      etree.SubElement(self.entry, ATOM + "title")
      etree.SubElement(self.entry, ATOM + "id")
      etree.SubElement(self.entry, ATOM + "updated")
      etree.SubElement(self.entry, ATOM + "content")
    else:
      self.entry = entry

    self.setTitle("Mail Filter")
    self.setID("")
    self.setUpdated("")
    self.setContent("")
 
  def setSingleText(self, key, text):
    element = self.entry.xpath('atom:' + key, namespaces=namespaces)[0]
    element.text = text

  def setTitle(self, text):
    self.setSingleText("title", text)
  
  def setID(self, text):
    self.setSingleText("id", text)
  
  def setUpdated(self, text):
    self.setSingleText("updated", text)
  
  def setContent(self, text):
    self.setSingleText("content", text)
 
  def getProperties(self):
    return self.entry.xpath('apps:property', namespaces=namespaces)
  
  def getProperty(self, name):
    return self.entry.xpath('apps:property[@name="{n}"]'.format(n=name), namespaces=namespaces)

  def newProperty(self, name, value):
    property = etree.SubElement(self.entry, APPS + "property")
    property.set("name", name)
    property.set("value", value)
    property.text = ""
