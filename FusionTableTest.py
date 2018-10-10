#!python3
#!python2
#encoding:utf-8

import os.path
import requests
import urllib.parse
import json
import GetAccessTokenFromRefreshToken
import datetime
client_id = "1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com"
client_secret = "TtvNOi4daznlLTjQJho66LwO"
api_key = 'AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0'
tableid = '1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
refresh_token = '1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc'
"""
client_id = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
client_secret = "bbbbbbbbbbbbbbbbbbbb"
api_key = 'ccccccccccccccccccc'
tableid = 'ddddddddddddddddddddddd'
refresh_token = 'eeeeeeeeeeeeeeeeeeee'
"""
class FusionTablesAPIRunner:
    def __init__(self):
        self.refresh_token = refresh_token
        self.access_token = ""
        self.token_file_path = "Google.OAuth2.AccessToken.{0}.json".format(client_id)

    def initialize(self):
        if os.path.exists(self.token_file_path):
            file = open(self.token_file_path, 'r', encoding='utf-8')
            j = json.loads(file.read())
            file.close()
            self.access_token = j["access_token"]
        else:
            self.request_new_access_token()

    def request_new_access_token(self):
        req = GetAccessTokenFromRefreshToken.AccessTokenRequester()
        token = req.get_token(client_id, client_secret, refresh_token)
        self.access_token = token["access_token"]
        
        file = open(self.token_file_path, 'w', encoding='utf-8')
        file.write(json.dumps(token))
        file.close()

    def insert_request(self):
        today = datetime.datetime.today()
        sql = "INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (tableid,"001",today,114)
        print(type(sql))
        #print(sql)
        #sql = "INSERT INTO %s (TimeStamp, CpuTemperature) values('%s',%s)" % (tableid, '2016-12-01 01:02:03',44444)
        headers={'Content-Type':'application/json'}
        data = {
            "sql": sql
        }
        url = 'https://www.googleapis.com/fusiontables/v2/query?' + 'key=' + urllib.parse.quote_plus(api_key) + '&' + 'access_token=' + urllib.parse.quote_plus(self.access_token) + '&' + 'sql=' + urllib.parse.quote_plus(sql)
        print(type(headers))
        print(type(data))
        print(url)
        print(type(sql))
        #return urllib.request.urlopen(url, data=data, headers=headers)
        #return urllib.request.Request(url,data=data,headers=headers)
        return requests.post(url,data=data,headers=headers)

    def insert(self):
        r = self.insert_request()
        
        if not(r.status_code == 200):
            print("Error: {0}\n".format(r.status_code))
            print(r.text)
            if (self.is_old_asscess_token(r)):
                self.request_new_access_token()
                r = self.insert_request()
                print(r.text)

        filePath = "Google.FusionTables.query.sql.insert.json"
        file = open(filePath, 'w', encoding='utf-8')
        file.write(r.text)
        file.close()

    def is_old_asscess_token(self, response):
        if (response.status_code == 401):
            j = json.loads(response.text)
            errors = j["error"]["errors"][0]
            if (errors["reason"] == "authError" and 
                errors["message"] == "Invalid Credentials" and
                errors["location"] == "Authorization"
            ):
                return True
            else:
                return False


if __name__ == "__main__":
    run = FusionTablesAPIRunner()
    run.initialize()
    run.insert()