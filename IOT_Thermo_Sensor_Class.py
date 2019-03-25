# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FileName   :IOT_Thermo_Sensor_Class.py
Description:IOT温度センサを動かす。
Written    :
Update     :
"""

"""
モジュールをインポートする。
"""
import serial
import smbus
import time
import RPi.GPIO as GPIO
import sys
import FusionTableInsert as Insert
import importlib
import datetime
import IOT_Thermo_Sensor_Key as Key

devID=["001","002","003","004","005","006","007","008","009","010"]

#FusionTablesID
tableid = Key.tableid
ERROR='ERROR'
count=0
bus = smbus.SMBus(1)#i2Cの設定
MICON_ADDRESS = 0x2c#マイコンのi2Cアドレス、ここでのアドレスはマイコンだと左に１ビットずれた状態になる。
SLAVE_ADDRESS = MICON_ADDRESS>>1#ややこしくなるので、こっちでも同じ数字で設定して、シフトでずらし問題がないようにする。
REGISTER_ADDRESS=0x13#マイコンのレジスタアドレス、仮で設定する。

read_flag=False
"""
Class Name :Command
Description:Send Comand
Argument   :
Return     :
Written    :
Update     :
"""

class Command:
    #初期化
    """
    FunctionName:init
    Description :initialization
    Argument    :self
    Return      :
    Written     :
    Update      :
    """
    def __init__(self):
        importlib.reload(Insert)
        self.requester=Insert.FusionTablesAPIRunner()
        self.requester.initialize()
    """
    FunctionName:init
    Description :Reading data from micro,and Execution by Command
    Argument    :self,read_flag
    Return      :test_mes,mes_mes,temp_num,ERROR
    Written     :
    Update      :
    """
    #マイコンから送られたデータを受け取って、コマンド(フラグ)別に処理するメソッド
    def R_Read(self,read_flag):
        
        reading=0
        #TEST通信
        if read_flag=='test':
        #4バイト分のデータを受信
            time.sleep(1)
            test=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,4)
            test_list=[]
            for i in range(4):
                test_list.insert(i,chr(test[i]))
            test_mes=''.join(test_list)
            #4バイトを文字列にして連結したものが
            return test_mes
            if test_mes=="TEST":
                #TESTの場合
                return test_mes
            else :
                #それ以外
                print("文字列を受信できませんでした")
                return "ERROR"
                
        #MEASURE通信   
        if read_flag=='ad':
            #受信した文字列
            msr=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,7)
            msr_list=[]
            
            #文字列を連結する
            for i in range(7):
                msr_list.insert(i,chr(msr[i]))
            #文字列が届いた場合
            if msr[0] is not 255:
                msr_mes=''.join(msr_list)
                return msr_mes
            #MEASUREが届かなかった場合
            else:
                
                print("計測結果を受信できませんでした")
                
                return "ERROR"
            
        #温度データ読み込みコマンド TEMP   
        if read_flag=='r':
            list_last=11
            time.sleep(1)
            temp=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,11)
            print(temp)
            temp_list=[]
            #文字列の中の温度部分を取り出して連結
            if temp[10] is 0 and temp[6] is not 48 and temp[9] is not 255:
                list_last=10
                
            for i in range(5,list_last):
                temp_list.insert(i,chr(temp[i]))
                temp_mes=''.join(temp_list)
            print(temp_mes)
            
            if temp[10] is 0 and temp[6] is not 48 and temp[9] is not 255:
                #温度の小数点以下二位が0のとき
                temp_mes=temp_mes.rstrip()
                print(temp_mes)
                #文字列の温度データを温度の部分だけ数字に
                temp_num=float(temp_mes)
                return temp_num
            
            if temp[10] is not 0 and temp[0] is not 255 and temp[10] is not 255:
                #文字列の温度データを温度の部分だけ数字に
                temp_num=float(temp_mes)
                return temp_num
            else:
                #うまく温度データを取り込めなかった場合
                print("温度データを取り込めませんでした。")
                #read_flag='ad'
                #Command().R_Read(read_flag)
                ERROR='ERROR'
                return (ERROR)
                
        else:
            #うまく温度データを取り込めなかった場合
            print("温度データを取り込めませんでした。")
            #read_flag='ad'
            #Command().R_Read(read_flag)
            ERROR='ERROR'
            return (ERROR)
        if read_flag=='else':
            pass

    """
    FunctionName:Task_Command
    Description :Sending Command
    Argument    :self,command
    Return      :None
    Written     :
    Update      :
    """
    #コマンドを入力して送信するメソッド
    def Task_Command(self,command):
        if command == 'measure':#AD変換
                #コマンド[MEASURE]を送信する
                time.sleep(0.1)
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                #フラグセット
                read_flag='ad'
                #受信処理
                measure=Command().R_Read(read_flag)
                print(measure)
                #返り値がMEASUREの場合
                if measure == "MEASURE":
                #TEMPをコマンドセットして実行
                    command='r'
                    Command().Task_Command(command)
                else:
                #それ以外の返り値の場合
                #MEASUREをコマンドセットして実行
                    command='measure'
                    Command().Task_Command(command)
        elif command == 'r':#温度データ呼び出し(READ_TEMP)
                #コマンド[READ_TEMP]を送信する
                time.sleep(1)
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
                #フラグセット
                read_flag='r'
                #受信処理
                read=Command().R_Read(read_flag)
                print(read)
                #返り値がERRORの場合
                if read =='ERROR':
                    #コマンドメジャーをセット
                    time.sleep(3)
                    command='measure'
                    Command().Task_Command(command)
                else:
                #返り値がTEMP=±○○.○○の場合
                    today = datetime.datetime.today()
                #日付の取得
                    print(today)
                    #SQL文を作成する
                    
                    sql = "INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (tableid,devID[2],today,read)
                    print(sql)
                    #SQL文をデータベース登録のモジュールに渡す。
                    request=self.requester.query(sql,is_write_response=True)
                    if request=="ERROR":
                    #返り値がERRORの場合
                        #コマンドMEASUREをセット
                        command="measure"
                        Command().Task_Command(command)
                    else:
                        time.sleep(50)

                    
        elif command == 'test':#TEST通信
                #コマンド[TEST]を送信する
                time.sleep(1)
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])  
                #フラグセット
                read_flag='test'
                #受信処理
                test=Command().R_Read(read_flag)
                
                #文字列がTESTの場合
                if test=='TEST':
                #MEASUREコマンド実行
                    print(test)
                    command='measure'
                    #command='r'measureより先にreadコマンドを送信する動作確認で必要になる.
                
                    Command().Task_Command(command)
                #文字列がERRORの場合    
                elif test=='ERROR':
                    print(test)
                #もう一度TESTコマンド実行
                    #time.sleep(0.1)
                    command='test'
                    Command().Task_Command(command)
    """
    FunctionName:main
    Description :Main Function
    Argument    :self count
    Return      :
    Written     :
    Update      :
    """
    def main(self,count):
        
        if count==0:
            print("初期化します")
            #初期化
            
            init=Insert.FusionTablesAPIRunner().initialize()
        if init=="ERROR":
            print("初期化に失敗しました")
            sys.exit()
        else :
            count=1
        time.sleep(10)
        command='test'
        Command().Task_Command(command)
        
                 
#メインループ              
while __name__=="__main__":
    #Command().main(count)
    """if count==0:
        print("初期化します")
        #初期化
        init=Insert.FusionTablesAPIRunner().initialize()
        if init=="ERROR":
            print("初期化に失敗しました")
            sys.exit()
        else :"""
    command='test'
    #command='measure'コマンドを送信する順番を変えて動作チェックをするときはこっちのmeasureコマンドを使う。
    Command().Task_Command(command)
    count=1
    #time.sleep(10)
    
    


