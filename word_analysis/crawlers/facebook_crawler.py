import facebook as fb
from word_analysis.models.entry import Entry

class FacebookCrawler(object):
   def __init__(self,token):
     self.api = fb.GraphAPI(token)

   def post_to_entry(post):
      return Entry()
   
