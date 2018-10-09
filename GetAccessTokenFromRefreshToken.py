#!python3
#encoding:utf-8

#標準ライブラリのインポート
import requests
import json
#クラス宣言
class AccessTokenRequester:
    def __init__(self):
        pass
    #アクセストークンを取得するメソッド
    def get_token(self, client_id, client_secret, refresh_token,is_debug_output=False):
        #データ群
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token"
        }
        #POST通信でアクセストークンを取得する
        r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
        
        if(is_debug_output):
            print(r.text)
        return json.loads(r.text);
    #アクセストークン取得実行
    def get_access_token(self, client_id, client_secret, refresh_token):
        j = self.get_token(client_id, client_secret, refresh_token)
        return j["access_token"]
