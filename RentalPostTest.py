import requests
import urllib.request
import urllib.parse
import json
#headers=
#riyousha=str("利用者");
data={"name":"利用者",
      "item":"工具",
      "rent":"2018/12/28",
      "reserve":"2018/12/28",
      "back":"2018/12/31"    
    }
url='https://script.google.com/macros/s/AKfycbzkLmXh29-CYlqOcfOFrmJNSt5y-Aw5pUOqEw8u-mB18fEoRnc6/exec'
r=requests.post(url,data=data)
print(r.status_code)
print(r.headers)

