
import os
import os.path
import json
from urlparse import urlparse

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web as web

import pymongo

from pymongo import MongoClient

from tornado.options import define, options

#from HTMLParser import HTMLParser (I don't think this links to anything but I forget)
from controllers import *

define("port", default=5000, help="run on the given port", type=int)

class Application(web.Application):
  def __init__(self):
    handlers=[
      (r'/', handler.MainHandler),
      (r'/jobs', handler.JobHandler)
      #(r'/payment', PaymentHandler)
    ]

    settings= dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True,
    )

    MONGO_URL = os.environ.get('MONGOHQ_URL')

    if MONGO_URL:
      # Get a connection
      self.conn = MongoClient(MONGO_URL)
      
      # Get the database
      self.db = self.conn[urlparse(MONGO_URL).path[1:]]
    else:
      # Not on an app with the MongoHQ add-on, do some localhost action
      self.conn = MongoClient("localhost", 27017)
      self.db = self.conn['wh_list']
    
    web.Application.__init__(self, handlers, **settings)  

#code from other application that I have not yet switched out. Will need to think about how jobs get rendered.
'''
class JobHandler(tornado.web.RequestHandler):
  def get(self):
    coll = self.application.db.test_collection
    jobs = coll.find()
    self.render(
      "index.html",
      title = "Contact Manager",
      header = "Real Estate Broker's Contact Manager",
      contacts = contacts
    )
  def post(self):
    import time
    contact_fields = ['name', 'email']
    coll= self.application.db.test_collection
    contacts = dict()
    for key in contact_fields:
      contacts[key] = self.get_argument(key, None)
    contacts['date_created'] = int(time.time())
    coll.insert(contacts)
    self.redirect("/index")
    '''
    
if __name__=='__main__':
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(os.environ.get("PORT", 5000))
  tornado.ioloop.IOLoop.instance().start()




