import sys
from lxml import etree
from StringIO import StringIO

class GmailFilters:

  # 21 Jul 2011 : GWA : Support loading from a pre-exported filter set or from scratch.
  
  namespaces = {'atom' : 'http://www.w3.org/2005/Atom',
                'apps' : 'http://schemas.google.com/apps/2006'}

  def __init__(self, string):
    if string != "":
      f = StringIO(string)
      self.tree = etree.parse(f)
      self.feed = self.tree.xpath('/atom:feed', namespaces=GmailFilters.namespaces)[0]
      title = self.tree.xpath('/atom:feed/atom:title', namespaces=GmailFilters.namespaces)[0]
      id = self.tree.xpath('/atom:feed/atom:id', namespaces=GmailFilters.namespaces)[0]
      updated = self.tree.xpath('/atom:feed/atom:updated', namespaces=GmailFilters.namespaces)[0]
    else:
      self.feed = etree.Element("feed")
      title = etree.SubElement(self.feed, "title")
      id = etree.SubElement(self.feed, "id")
      updated = etree.SubElement(self.feed, "updated")
      author = etree.SubElement(self.feed, "author")
      name = etree.SubElement(author, "name")
      email = etree.SubElement(author, "email")
      name.text = ""
      email.text = ""

    title.text = "Mail Filters"
    id.text = ""
    updated.text = ""

  def __repr__(self):
    return etree.tostring(self.feed, xml_declaration=True, encoding="utf-8", pretty_print=True)
