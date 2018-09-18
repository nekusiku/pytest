#!python3
#encoding:utf-8

import requests

from datetime import datetime
from urllib.parse import urlparse
import urllib.request, urllib.parse
appsScriptdevId = 'AKfycby1XNBOWqfjtCysPqwI3l6haQFzFBXQAXiaPBNGhmuSy8g7povS/exec'
devURL='https://script.google.com/macros/s{0}/dev'.format(appsScriptdevId)
url=devURL
u=urlparse(url)
print(u)


input_params=urllib.parse.urlencode({"TimeStamp":"2000-01-01 00:11:22","CpuTemperature":"30000"})

r=requests.get(url,params=input_params)
print(u)
print(r)


filename = "Response.txt"
file = open(filename, 'w', encoding="UTF-8")

file.write(r.text)
file.close()
