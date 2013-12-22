import word_analysis.database.driver as db

class Result(object):
  def map_fun(self):
     return '''function(doc) {
       if (doc.processed_text) {
         doc.processed_text.forEach(function(element) {
           emit([element[0].toLowerCase(),element[1]],{count: 1});
         });
       }
     }'''
  def reduce_fun(self):
     return '''function(key,values,rereduce) {
       var sum = 0;
       for(i=0; i < values.length; i++) {
         sum = sum + values[i].count;
       }
       return({count: sum});
     }'''

  def query(self):
    return db.db.query(self.map_fun(),reduce_fun=self.reduce_fun(),group=True)

  def run(self):
     for row in self.query():
        print row
