#!python2
#encoding:utf-8

import urllib2, urllib, simplejson, sys, httplib
import codecs

client_id = "1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com"
client_secret = "TtvNOi4daznlLTjQJho66LwO"
redirect_uri = "http://localhost:8000"

class RunAPITest:
  def __init__(self):
      pass

  def main(self):
      print "copy and paste the url below into browser address bar and hit enter"
      print "https://accounts.google.com/o/oauth2/auth?%s%s%s%s" % \
            ("client_id=%s&" % (client_id),
             "redirect_uri=%s&" % (redirect_uri),
             "scope=https://www.googleapis.com/auth/fusiontables&",
             "response_type=code")
      code = raw_input("Enter code (parameter of URL): ")
      data = urllib.urlencode({
          "code": code,
          "client_id": client_id,
          "client_secret": client_secret,
          "redirect_uri": redirect_uri,
          "grant_type": "authorization_code"
          })
      serv_req = urllib2.Request(url="https://accounts.google.com/o/oauth2/token",
                                 data=data)
      serv_resp = urllib2.urlopen(serv_req)
      response = serv_resp.read()
      filePath = "Google.OAuth2.Token.{0}.json".format(client_id)
      file = codecs.open(filePath, 'w', 'utf-8')
      file.write(response)
      file.close()
    
if __name__ == "__main__":
    api_test = RunAPITest()
    api_test.main()