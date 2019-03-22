#!/usr/bin/env python

#-*- coding: utf-8 -*-
import serial
import smbus
import time
import RPi.GPIO as GPIO
import sys
import FusionTableInsert as Insert
import importlib
import datetime


tableid = '1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
count = 0
bus = smbus.SMBus(1)#i2Cの設定
MICON_ADDRESS = 0x2c#マイコンのi2Cアドレス、ここでのアドレスはマイコンだと左に１ビットずれた状態になる。
SLAVE_ADDRESS = MICON_ADDRESS>>1#ややこしくなるので、こっちでも同じ数字で設定して、シフトでずらし問題がないようにする。
REGISTER_ADDRESS=0x13#マイコンのレジスタアドレス、仮で設定する。

read_flag=False 

class Command:
    #初期化
    def __init__(self):
        importlib.reload(Insert)
        self.requester=Insert.FusionTablesAPIRunner()
        self.requester.initialize()
    
    #マイコンから送られたデータを受け取って、コマンド別に処理するメソッド
    def R_Read(self,read_flag):
        
        reading=0
        #TEST通信
        if read_flag=='test':
            time.sleep(0.01)
            test=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,4)
            test_list=[]
            for i in range(4):
                test_list.insert(i,chr(test[i]))
            test_mes=''.join(test_list)
            print(test_mes)
            time.sleep(1)
            command='measure'
            Command().Task_Command(command)
        #MEASURE通信   
        if read_flag=='ad':
            #受信した文字列
            time.sleep(0.3)
            msr=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,7)
            msr_list=[]
            #文字列を連結する
            for i in range(7):
                msr_list.insert(i,chr(msr[i]))
            #文字列が届いた場合
            print(msr_list)
            if msr[0] is not 255:
                msr_mes=''.join(msr_list)
                print(msr_mes)
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
                command='r'
                time.sleep(0.1)
                Command().Task_Command(command)
                #read_flag='r'
                #Command().R_Read(read_flag)
            #MEASUREが届かなかった場合
            else:
                #sys.exit()
                print("数秒待って入力してくださいM")
                #time.sleep(1)
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                #read_flag='ad'
                #Command().R_Read(read_flag)
                #Command().Task_Command()
            
        #温度データ読み込み    
        if read_flag=='r':
            time.sleep(0.01)
            temp=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,11)
            print(temp)
            temp_list=[]
            #文字列の中の温度部分を取り出して連結
            for i in range(5,11):
                temp_list.insert(i,chr(temp[i]))
                temp_mes=''.join(temp_list)
            print(temp_mes)
            if temp[10] is not 0 and temp[0] is not 255:
                #文字列の温度データを温度の部分だけ数字に
                temp_num=float(temp_mes)
                
                #日付の取得
                today = datetime.datetime.today()
                print(today)
                print(type(today))
                #SQL文を作成する
                
                sql = "INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (tableid,"002",today,temp_num)
                
                #SQL文をデータベース登録のモジュールに渡す。
                self.requester.query(sql,is_write_response=True)
                time.sleep(60)
            else :
                #sys.exit()
                #うまく温度データを取り込めなかった場合
                #break
                print("数秒待って入力してください")
                time.sleep(1)
                
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                #read_flag='ad'
                #Command().R_Read(read_flag)
                #read_flag='r'
                #print(read_flag)
                pass
            
        if read_flag=='else':
            pass
        
    #コマンドを入力して送信するメソッド
    def Task_Command(self,command):
        #command = 0    
        #command = input("[温度計測：MEASURE][温度データ取得:r][テスト通信:TEST] 入力コマンド:")#コマンド入力
        if command == 'measure':#AD変換
                #コマンド[MEASURE]を送信する
                print("measure")
                
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                read_flag='ad'
                time.sleep(0.1)
                Command().R_Read(read_flag)
            
             
        elif command == 'r':#温度データ呼び出し(READ_TEMP)
                #コマンド[READ_TEMP]を送信する
                
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
                read_flag='r'
                print(read_flag)
                print("commad_read")
                Command().R_Read(read_flag)
                
        elif command == 'test':#TEST通信
                #コマンド[TEST]を送信する
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])  
                read_flag='test'
                Command().R_Read(read_flag)
#メインループ              
while __name__=="__main__":
    print("hoge")
    command='measure'
    Command().Task_Command(command)
    print("huga")
   

