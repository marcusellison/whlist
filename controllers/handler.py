from base import *

from ui_modules import nyc_zipcode

# -------------------------------------------------------------------
# Main Handler
# -------------------------------------------------------------------

class MainHandler(web.RequestHandler):
  def get(self):
    self.render("index.html",
    title = "WHListed"
    )

# -------------------------------------------------------------------
# Jobs Page Handler
# -------------------------------------------------------------------

class JobHandler(web.RequestHandler):
  def post(self):

    try:
      zipcode = int(self.get_argument('zipcode'))
      if nyc_zipcode(zipcode):
        data = json.load(urllib2.urlopen('http://www.authenticjobs.com/api/?api_key=d75d50a373f9db1655ff1dfb7fc891d8&method=aj.jobs.search&type=2&format=json'))
        jobs = data["listings"]["listing"]
        self.render(
         "jobs.html",
          title = "WHListed",
          jobs = jobs,
          zipcode = zipcode
        )
      else:
        self.render(
          "coming_soon.html",
          title="WHListed"
        )
    except ValueError:
      self.render(
          "form_error.html",
          title="WHListed"
        )

    



  '''def get(self):
    data = json.load(urllib2.urlopen('http://www.authenticjobs.com/api/?api_key=d75d50a373f9db1655ff1dfb7fc891d8&method=aj.jobs.search&type=2&format=json'))
    jobs = data["listings"]["listing"]

    self.render("jobs.html",
    title = "WHListed",
    jobs = jobs
    )'''