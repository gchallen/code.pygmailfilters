class GMailFilter:
  import re  
  matchmatch = re.compile("Matches:.*?<b>(.*?)</b>")
  actionmatch = re.compile("Do this: (.*)")

  # 20 Jul 2011 : GWA : Actions without parameters.

  archivematch = re.compile("Skip Inbox")
  deletematch = re.compile("Delete it")

  # 20 Jul 2011 : GWA : Actions with parameters.

  forwardmatch = re.compile("Forward to (.*)")
  labelmatch = re.compile("Apply label \"(.*?)\"")

  def __init__(self, match, archive, delete, label, forward):
    self.match = match
   
    self.archive = archive
    self.delete = delete

    self.label = label
    self.forward = forward

  @classmethod
  def fromSoup(cls, soup):
    toreturn = []
    for i in soup.findAll("div", "begin-container"):
      toreturn.append(cls.fromString(str(i)))
    return toreturn

  @classmethod
  def fromString(cls, string):

      match = None
      archive = False
      delete = False
      label = None
      forward = None

      m = cls.matchmatch.search(string)
      if m != None:
        match = m.group(1)

      m = cls.actionmatch.search(string)
      if m != None:
        actions = m.group(1)
      if cls.archivematch.search(actions) != None:
        archive = True
      if cls.deletematch.search(actions) != None:
        delete = True
      m = cls.labelmatch.search(actions)
      if m != None:
        label = m.group(1)
      m = cls.forwardmatch.search(actions)
      if m != None:
        forward = m.group(1)

      return GMailFilter(match, archive, delete, label, forward)
