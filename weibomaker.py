# -*- coding: utf-8 -*-
import webapp2
import urllib2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        key = self.request.get('key')
        value1 = self.request.get('value1')
        value2 = self.request.get('value2')
        value1 = value1.encode('utf-8')
        value2 = value2.encode('utf-8')
        value1 = urllib2.quote(value1)
        value2 = urllib2.quote(value2)
        self.response.write(value1+' VS '+value2+'\n')
        if value2=='':
            url = "https://maker.ifttt.com/trigger/makertext2twitter/with/key/"+key+"?value1="+value1
        else:
            url = "https://maker.ifttt.com/trigger/makerpic2twitter/with/key/"+key+"?value1="+value1+"&value2="+value2
        self.response.write(url+'\n')
        try:
            response = urllib2.urlopen(url, data="")
            self.response.write(response.read())
            response.close()
        except urllib2.URLError, e:
            self.response.write(e.code)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
