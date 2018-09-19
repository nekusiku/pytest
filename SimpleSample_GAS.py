#!python2
# https://developers.google.com/fusiontables/docs/samples/python

import urllib2, urllib, simplejson, sys, httplib

client_id="1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com"
client_secret="TtvNOi4daznlLTjQJho66LwO"
redirect_uri = "http://localhost:8000"
api_key = "AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0"
tableid = "1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH"

class RunAPITest:
  def __init__(self):
    self.access_token = ""
    self.params = ""

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
    tokens = simplejson.loads(response)
    access_token = tokens["access_token"]
    self.access_token = access_token
    self.params = "?key=%s&access_token=%s" % \
      (api_key, self.access_token)

  def testInsertV2(self):
    print "v2 Query.sql insert"
    sql = "INSERT INTO %s (TimeStamp, CpuTemperature) values('%s',%s)" % (tableid, '2011-11-11 11:11:11',11111)
    data = '''{
      "sql": "%s"
    }''' % (sql)
    response = self.runRequest(
      "POST",
      "/fusiontables/v2/query%s&sql=%s" % \
       (self.params, urllib.quote(sql)),
      data=data,
      headers={'Content-Type':'application/json'})
    json_response = simplejson.loads(response)
    print(json_response)
    return json_response

  def runRequest(self, method, url, data=None, headers=None):
    request = httplib.HTTPSConnection("www.googleapis.com")

    if data and headers: request.request(method, url, data, headers)
    else: request.request(method, url)
    response = request.getresponse()
    print response.status, response.reason
    response = response.read()
    print response
    return response

if __name__ == "__main__":
  api_test = RunAPITest()
  api_test.main()
  api_test.testInsertV2()