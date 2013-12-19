class Entry(object):

  @classmethod
  def from_database(id):
    # fetch and create entry from database connector
    return Entry()

  @property
  def text(self):
    return self._text

  @text.setter
  def text(self,v):
    self._text = v

  # source media ( fb, ask.fm.. )
  @property
  def source(self):
    return self._source
  
  @source.setter
  def source(self,v):
     self._source = v
  
  @property
  def author(self): 
    return self._author

  @author.setter
  def author(self,v):
    self._author = v

  # link of the entry
  @property
  def link(self):
    return self._link

  @link.setter
  def link(self,v):
    self._link = v
  
  @property
  def id(self):
    return self._id

  @id.setter
  def id(self,v):
    self._id = v

  def save(self):
    return self.id

  def delete(self):
    return self.id
    
  def process(self):
    # pos tag, stem
    return None
    
