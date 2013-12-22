import facebook as fb
import itertools
from word_analysis.models.entry import Entry
from word_analysis.config.config import config
from word_analysis.crawlers.crawler import Crawler

default_token = config()['facebook']['app_user_token']

class FacebookCrawler(Crawler):
   def __init__(self,token = default_token):
     self.api = fb.GraphAPI(token)

   def search(self,term):
     return self.api.get_object("search", q=term)
   def post_to_entry(self,post):
      e = Entry()
      e.text = post.get('message',None)
      e.user = post.get('from', None)
      e.id = post['id']
      e.process_text()
      if e.text:
        e.save()
      return e
   
class FacebookQueryTermCrawler(FacebookCrawler):
  def __init__(self,query_terms,token = default_token):
    self.api = fb.GraphAPI(token)
    self.query_terms = query_terms
    

  def search(self,term):
    return self.api.get_object("search", q=term, type='post')['data']

  def perform(self):
    return map(self.post_to_entry,list(itertools.chain.from_iterable(map(self.search, self.query_terms))))

