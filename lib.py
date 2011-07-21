import sys
from lxml import etree
from StringIO import StringIO

class GmailFilters:

  # 21 Jul 2011 : GWA : Support loading from a pre-exported filter set or from scratch.

  def __init__(self, string):
    if string != "":
      f = StringIO(string)
      self.tree = etree.parse(f)
      name = self.feed.xpath("/feed/name")
      id = self.feed.xpath("/feed/id")
      updated = self.feed.xpath("/feed/updated")
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
