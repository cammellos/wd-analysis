import couchdb
import word_analysis.config.config as config

couch = couchdb.Server(config.config()['database']['host'] + ':' + config.config()['database']['port'])
try:
  db = couch.create(config.config()['database']['name'])
except couchdb.PreconditionFailed:
  db = couch[config.config()['database']['name']]

def get(key):
  return db[key]

def save(key,json):
   db[key] = json

def delete(key):
   db.delete(db[key])
