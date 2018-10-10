#!python3
#!python2
#encoding:utf-8

#Python標準ライブラリのモジュールをimport
import os.path
import requests
#from urllib import request
import urllib.request
import urllib.parse
import importlib
import json
import datetime

#作成したモジュールをimport

#アクセストークンをインポートするモジュール
import GetAccessTokenFromRefreshToken as GetAccess
#マイコンと通信するモジュール
import IOT_Thermo_Sensor_Class as IOT


#クラス宣言
class FusionTablesAPIRunner:
    #FusionTableの認証の初期化
    def __init__(self):
        self.token_requester=None
        self.api_key=None
        self.client_id = None
        self.client_secret = None
        self.refresh_key = None
        self.access_key = None
        self.refresh_token=None
    #認証の初期設定
    def initialize(self):
        #OAuth2.0認証
        self.client_id='1033655159638-fek1o17voj7hfut8hggaffceh1bab4po.apps.googleusercontent.com'
        self.client_secret='TtvNOi4daznlLTjQJho66LwO'
        #APIキー
        self.api_key='AIzaSyDJntsUxTlr6nOUTDqOuynw8OyJGw9Tai0'
        #データベースのID
        self.tableid='1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
        #APIを使うためのトークン
        self.refresh_token='1/FUAfwIr9_ZvjTCiqHX6-BApngOVuaVWylClw80U8Tlc'
        self.token_requester=GetAccess.AccessTokenRequester()
        self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
  

    #データベース登録の実行文を呼び出し
    def query(self,sql,is_write_response=False):
        r = self._query_request(sql)
        print(r)
        #通信がうまく行かなくなった場合の処理
        if not(r.status_code == 200):
            #エラーメッセージの表示
            print("Error: {0}\n".format(r.status_code))
            print(r.text)
            if (self.is_old_asscess_token(r)):
                self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
                r = self._query_request(sql)
                print(r.text)
                
        if(is_write_response):
            filePath = "Google.FusionTables.query.sql.insert.json"
            file = open(filePath, 'w', encoding='utf-8')
            file.write(r.text)
            file.close()
    #データベース登録の実行文
    def _query_request(self,sql):
        #日付処理
        today = datetime.datetime.today()
        #ヘッダーの設定
        headers={'Content-Type':'application/json'}
        #データにsql文を設定
        sql_data = {
            "sql": sql
        }
        sql_enc_data=urllib.parse.urlencode(sql_data).encode('utf-8')
        #urlの設定
        
        url=(
            'https://www.googleapis.com/fusiontables/v2/query?'+
            'key=' + urllib.parse.quote(self.api_key)+'&'+
            'access_token=' + urllib.parse.quote(self.access_token)+'&'+
            'sql=' + urllib.parse.quote(sql)
            )
            
        #POST通信(Url,ヘッダー,データ)returnでレスポンスが表示される
        #return requests.post(url,headers=headers,data=sql_data)
        req = urllib.request.Request(url,sql_enc_data,headers)
        response = urllib.request.urlopen(req)
        html=response.read()#レスポンスボディ
        return html.decode('utf-8')
    
    #古いアクセストークンの場合の処理
    def is_old_asscess_token(self, response):
        #レスポンスが401(認証が拒否された)のとき
        if (response.status_code == 401):
            j = json.loads(response.text)
            errors = j["error"]["errors"][0]
            if (errors["reason"] == "authError" and
                errors["message"] == "Invalid Credentials" and
                errors["location"] == "Authorization"):
                return True
            else:
                return False
if __name__ == "__main__":
    run = FusionTablesAPIRunner()
    run.initialize()
    run.query()