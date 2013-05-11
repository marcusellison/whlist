import os.path
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web as web

import pymongo

from pymongo import MongoClient

from tornado.options import define, options

#from HTMLParser import HTMLParser (I don't think this links to anything but I forget)
from controllers import *

define("port", default=8000, help="run on the given port", type=int)

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

    client = MongoClient("localhost", 27017)
    self.db = client.wh_list
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
#class PaymentHandler(tornado.web.RequestHandler):
# def post(self):
#   payment_fields = ['id', 'card', 'created' , 'currency', 'livemode', 'object', 'used']
#   coll = self.application.db.contact
#   contacts = dict()
    
if __name__=='__main__':
  tornado.options.parse_command_line()
  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(options.port)
  tornado.ioloop.IOLoop.instance().start()




