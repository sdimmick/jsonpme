#!/usr/bin/env python
import urllib
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):
    def get(self):
        # query string parameters
        url = self.request.get('url')
        callback = self.request.get('callback')
        
        if len(url) == 0 or len(callback) == 0:
            self.response.out.write('usage: http://jsonpme.appspot.com/?callback=[function_name]&url=[json_url]')
        else:
            try:
                # open the URL
                f = urllib.urlopen(url)
                json = f.read()
                          
                # wrap the JSON in a function call
                jsonp = callback + '(' + json + ')'
        
                # write response
                self.response.headers.add_header('Content-Type', 'text/javascript')
                self.response.out.write(jsonp)
            except IOError:
                # error retrieving data from specified URL
                self.response.set_status(500)
                self.response.out.write("Error opening URL: " + url)            

def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
