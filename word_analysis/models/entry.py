import nltk
import word_analysis.database.driver as db

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

  @property
  def processed_text(self):
    return self._processed_text

  @processed_text.setter
  def processed_text(self,v):
     self._processed_text = v

  def to_database(self):
    return {
      'id': self.id,
      'processed_text': self.processed_text,
    }

  def save(self):
    db.save(self.id,self.to_database())

  def delete(self):
    db.delete(self.id)
    
  def process_text(self):
    self.processed_text = nltk.pos_tag(nltk.word_tokenize(self.text))
    #self.processed_text = map(list,nltk.pos_tag(nltk.word_tokenize(self.text)))


    
