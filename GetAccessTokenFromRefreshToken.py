#!python3
#encoding:utf-8

import requests
import json

class AccessTokenRequester:
    def __init__(self):
        pass
    
    def get_token(self, client_id, client_secret, refresh_token):
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
        r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
        return json.loads(r.text);
    
    def get_access_token(self, client_id, client_secret, refresh_token):
        j = get_token(self, client_id, client_secret, refresh_token)
        return j["access_token"]
