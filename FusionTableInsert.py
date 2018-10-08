#!python3
#!python2
#encoding:utf-8

import os.path
import requests
import urllib.parse
import importlib
import json
import datetime

#他のモジュールよりimport
import GetAccessTokenFromRefreshToken as GetAccess
import IOT_Thermo_Sensor_Class as IOT
"""
client_id='1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com'
client_secret='TtvNOi4daznlLTjQJho66LwO'
api_key='AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0'
tableid='1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
refresh_token='1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc'
"""


class FusionTablesAPIRunner:
    def __init__(self):
        self.token_requester=None
        self.api_key=None
        self.client_id = None
        self.client_secret = None
        self.refresh_key = None
        self.access_key = None

        
        self.refresh_token=None
        #self.access_token=""
        #self.token_file_path="Google.OAuth2.AccessToken.{0}.json".format(self.client_id)

    def initialize(self):
        self.client_id='1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com'
        self.client_secret='TtvNOi4daznlLTjQJho66LwO'
        self.api_key='AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0'
        self.tableid='1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
        self.refresh_token='1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc'
        self.token_requester=GetAccess.AccessTokenRequester()
        self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
  
    """
        if os.path.exists(self.token_file_path):
            file = open(self.token_file_path, 'r', encoding='utf-8')
            j = json.loads(file.read())
            file.close()
            self.access_token = j["access_token"]
        else:
            self.request_new_access_token()
    """
    """
        def request_new_access_token(self):
        req = GetAccess.AccessTokenRequester()
        token = req.get_token(client_id, client_secret, refresh_token)
        self.access_token = token["access_token"]
        
        file = open(self.token_file_path, 'w', encoding='utf-8')
        file.write(json.dumps(token))
        file.close()
    """
    def query(self,sql,is_write_response=False):
        r = self._query_request(sql)
        #print(r.text)
        print(r.text)
        if not(r.status_code == 200):
            print("Error: {0}\n".format(r.status_code))
            print(r.text)
            if (self.is_old_asscess_token(r)):
                #self.request_new_access_token()
                self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
                r = self._query_request(sql)
                print(r.text)
                
        if(is_write_response):
            filePath = "Google.FusionTables.query.sql.insert.json"
            file = open(filePath, 'w', encoding='utf-8')
            file.write(r.text)
            file.close()
    
    def _query_request(self,sql):
        today = datetime.datetime.today()
        print("today_type_is")
        print(type(today))
        #sql="INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (self.tableid,"001",today,114)
        print("sql_type_before_is")
        print(type(sql))
        print(sql)
        #s=urllib.parse.urlencode(sql)
        headers={'Content-Type':'application/json'}
        print("headers_type_is")
        print(type(headers))
        sql_data = {
            "sql": sql
        }
        
        print("sql_type_is")
        print(type(sql_data))
        print(type(sql))
        url=(
            'https://www.googleapis.com/fusiontables/v2/query?'+
            'key=' + urllib.parse.quote(self.api_key)+'&'+
            'access_token=' + urllib.parse.quote(self.access_token)+'&'+
            'sql=' + urllib.parse.quote(sql)
            )
        print("sql_type_after_is")
        print(type(sql))
        print(url)
        print("url_type_is")
        print(type(url))
        print("Request")
        #return requests.post(url,data=data,headers=headers)
        return requests.post(url,headers=headers,data=sql_data)
        #return urllib.urlopen(url, data=sql_data, headers=headers)
        #return urllib.request.urlopen(url,data=data)
        #return urllib.request.Request(url,data=data,headers=headers)
        #return requests.post(url,data=data,headers=headers)
    

    def is_old_asscess_token(self, response):
        if (response.status_code == 401):
            j = json.loads(response.text)
            errors = j["error"]["errors"][0]
            if (errors["reason"] == "authError" and
                errors["message"] == "Invalid Credentials" and
                errors["location"] == "Authorization"):
                return True
            else:
                return False