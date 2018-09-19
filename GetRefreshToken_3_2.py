# ソースコード
#!python3
#encoding:utf-8

import requests
import json

class RefreshTokenRequester:
    def __init__(self):
        pass
    
    def get_access_token(self, client_id, client_secret, refresh_token):
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
        r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
        refresh_json = json.loads(r.text);
        return refresh_json["access_token"]

if __name__ == "__main__":
    client_id = "1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com"
    client_secret = "TtvNOi4daznlLTjQJho66LwO"
    refresh_token = "1/9_qs3UqrQcAf5iDmM9s1WE2ej-Wd2cgSqZmwT-L8shI"
    
    requester = RefreshTokenRequester()
    access_token = requester.get_access_token(client_id, client_secret, refresh_token)
    print(access_token)