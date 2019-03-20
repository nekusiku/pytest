# -*-coding:utf-8-*-
# !python3
"""
FileName   :FusionTableInsert.py
Description:データ登録機能
Written    :
Update     :
"""

#Python標準ライブラリのモジュールをimport
import os.path
import requests
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
import GoogleKeysGetter
#認証キーの外部ファイル
import IOT_Thermo_Sensor_Key as Key
#クラス宣言
"""
Class Name :FusionTablesAPIRunner
Description:Insert Date to DataTable by Use FusionTable Api
Argument   :
Return     :
Written    :
Update     :
"""
class FusionTablesAPIRunner:
    #FusionTableの認証の初期化
    """
    Class Name :init
    Description:initialization
    Argument   :self
    Return     :
    Written    :
    Update     :
    """
    def __init__(self):
        self.token_requester=None
        self.api_key=None
        self.client_id = None
        self.client_secret = None
        self.refresh_key = None
        self.access_key = None
        self.refresh_token=None
    #認証の初期設定
    """
    FunctionName:initializse
    Description :Certification Oauth2.0
    Argument    :self
    Return      :ERROR
    Written     :
    Update      :
    """
    def initialize(self):
        #OAuth2.0認証
        
        self.client_id=Key.client_id
        #クライアントID
        self.client_secret=Key.client_secret
        #APIキー
        
        self.api_key=Key.api_key
        #データベースのID
        
        self.tableid=Key.tableid
        #APIを使うためのトークン
        
        self.refresh_token=Key.refresh_token
        self.token_requester=GetAccess.AccessTokenRequester()
        #リフレッシュトークンからアクセストークンを取得する
        self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
        if(self.client_id is None):
            print("外部ファイルを読み込めませんでした")
            
            return "ERROR"
        if(self.client_secret is None):
            print("外部ファイルを読み込めませんでした")
            return "ERROR"
        if(self.api_key is None):
            print("外部ファイルを読み込めませんでした")
            return "ERROR"
        if(self.tableid is None):
            print("外部ファイルを読み込めませんでした")
            return "ERROR"

            
    """
    FunctionName:query
    Description :Call Function 
    Argument    :self,sql,is_write_response
    Return      :ERROR
    Written     :
    Update      :
    """
    #データベース登録の実行文を呼び出し
    def query(self,sql,is_write_response=False):
        r = self._query_request(sql)
        print(r.text)
    
        #通信がうまく行かなくなった場合の処理
        if not(r.status_code == 200):
            #エラーメッセージの表示
            print("Error: {0}\n".format(r.status_code))
            print(r.text)
            if (self.is_old_asscess_token(r)):
                self.access_token=self.token_requester.get_access_token(self.client_id,self.client_secret,self.refresh_token)
                r = self._query_request(sql)
                print(r.text)
                return "ERROR"
            #エラーメッセージの場合ERRORを返す。
        if(is_write_response):
            filePath = "Google.FusionTables.query.sql.insert.json"
            file = open(filePath, 'w', encoding='utf-8')
            file.write(r.text)
            file.close()
    """
    FunctionName:query_request
    Description :Execution Statement whitch Insert Data to DateBase 
    Argument    :self,sql
    Return      :requestpost,True,False
    Written     :
    Update      :
    """
    #データベース登録の実行文
    def _query_request(self,sql):
        #日付処理
        #today = datetime.datetime.today()
        #ヘッダーの設定
        headers={'Content-Type':'application/json'}
        #データにsql文を設定
        sql_data = {
            "sql": sql
        }
        #sql文をエンコード
        sql_enc_data=urllib.parse.urlencode(sql_data).encode('utf-8')
        
        #urlの設定
        url=(
            'https://www.googleapis.com/fusiontables/v2/query?'+
            'key=' + urllib.parse.quote(self.api_key)+'&'+
            'access_token=' + urllib.parse.quote(self.access_token)+'&'+
            'sql=' + urllib.parse.quote(sql)
            )
        print(url)    
        #POST通信(Url,ヘッダー,データ)returnでレスポンスが表示される
        return requests.post(url,headers=headers,data=sql_data)
    """
    FunctionName:is_old_access_token
    Description :processing Old AccessToken 
    Argument    :self,response
    Return      :True,False
    Written     :
    Update      :
    """    
    #古いアクセストークンの場合の処理
    def is_old_access_token(self,response):
        #レスポンスが401(認証が拒否された)のとき
        if (response == 401):
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
    run.query(sql)