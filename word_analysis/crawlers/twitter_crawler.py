import twitter as tw
import itertools
from word_analysis.models.entry import Entry
from word_analysis.config.config import config
from word_analysis.crawlers.crawler import Crawler

default_credentials = config()['twitter']
class TwitterCrawler(Crawler):
   def __init__(self,geocode = "37.781157,-122.398720,1mi",locale = "it", credentials = default_credentials):
     self.geocode = geocode
     self.locale = locale
     self.api = tw.Api(consumer_key=credentials['consumer_key'],consumer_secret=credentials['consumer_secret'],access_token_key=credentials['access_token_key'],access_token_secret=credentials['access_token_secret'])

   def search(self):
     return self.api.GetSearch(geocode=self.geocode)
   def post_to_entry(self,post):
      e = Entry()
      e.text = post.get('message',None)
      e.user = post.get('from', None)
      return e 
   def perform(self):
     return map(self.post_to_entry,list(itertools.chain.from_iterable(map(self.search, self.query_terms))))
