import sys
import pycurl

class Test:
   def __init__(self):
       self.contents = ''

   def body_callback(self, buf):
       self.contents = self.contents + buf

print >>sys.stderr, 'Testing', pycurl.version

t = Test()
c = pycurl.Curl()
c.setopt(c.URL, 'http://curl.haxx.se/dev/')
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
c.close()

print t.contents