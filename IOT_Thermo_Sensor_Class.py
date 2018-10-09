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
    
    #マイコンから送られたデータをコマンド別に処理するメソッド
    def R_Read(self,read_flag):
        reading=0
        #TEST通信
        if read_flag=='test':
            
            test=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,4)
            test_list=[]
            for i in range(4):
                test_list.insert(i,chr(test[i]))
            test_mes=''.join(test_list)
            print(test_mes)
        #MEASURE通信   
        if read_flag=='ad':
            #受信した文字列
            msr=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,7)
            print(msr)
            msr_list=[]
            for i in range(7):
                msr_list.insert(i,chr(msr[i]))
            if msr[0] is not 255:
                msr_mes=''.join(msr_list)
                print(msr_mes)
            #MEASUREが届かなかった場合
            else:
                print("数秒待って入力してください")
            
        #温度データ読み込み    
        if read_flag=='r':
            temp=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,11)
            temp_list=[]
            for i in range(5,11):
                temp_list.insert(i,chr(temp[i]))
                temp_mes=''.join(temp_list)
            print(temp_mes)
            if temp[10] is not 0 and temp[0] is not 255:
                #文字列の温度データを温度の部分だけ数字に
                temp_num=float(temp_mes)
                Sql_Temp=temp_num
                today = datetime.datetime.today()
                #SQL文を作成する
                
                sql="INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (tableid,"001",today,temp_num)
                #SQL文をデータベース登録のモジュールに渡す。
                self.requester.query(sql,is_write_response=True)
            else :
                #うまく温度データを取り込めなかった場合
                print("数秒待って入力してください")
                pass
            
        if read_flag=='else':
            pass
        
    #コマンドを入力して送信するメソッド
    def Task_Command(self):
        command = 0    
        command = input("[温度計測：MEASURE][温度データ取得:r][テスト通信:TEST] 入力コマンド:")#コマンド入力
        if command == 'measure':#AD変換
                #コマンド[MEASURE]を送信する
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                time.sleep(0.8)
                read_flag='ad'
                
                Command().R_Read(read_flag)
            
             
        elif command == 'r':#温度データ呼び出し(READ_TEMP)
                #コマンド[READ_TEMP]を送信する
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
                read_flag='r'
                Command().R_Read(read_flag)
                
        elif command == 'test':#TEST通信
                #コマンド[TEST]を送信する
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])  
                read_flag='test'
                Command().R_Read(read_flag)
              
while __name__=="__main__":
    Command().Task_Command()

