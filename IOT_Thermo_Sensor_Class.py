#!/usr/bin/env python

#-*- coding: utf-8 -*-
import serial
import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
import sqlite3
import FusionTableInsert as Insert
import importlib
import datetime
from enum import IntEnum

TaskName=['Init','Wait','ReadStart','ReadWait','ReadEnd','SendWait']
tableid = '1MNHaJ5Y9GbvSjAzXgI7_ww2sszbYIc88O2MYdewH'
count = 0
bus = smbus.SMBus(1)#i2Cの設定
MICON_ADDRESS = 0x2c#マイコンのi2Cアドレス、ここでのアドレスはマイコンだと左に１ビットずれた状態になる。
SLAVE_ADDRESS = MICON_ADDRESS>>1#ややこしくなるので、こっちでも同じ数字で設定して、関数でずらし問題がないようにする。
REGISTER_ADDRESS=0x13#マイコンのレジスタアドレス、仮で設定する。
#print(hex(MICON_ADDRESS))
#print(hex(SLAVE_ADDRESS))
#print(hex(REGISTER_ADDRESS))
register_read = 0x2c#読み込み用デバイスレジスタアドレス
register_write= 0x1e#書き込み用デバイスレジスタアドレス
_Command = 0x00
_Data=0x40
#_Config =0b
send_flag=False
read_flag=False

Read_Wait_Flag =False
Send_Wait_Flag =False
#def Read_CallBack:
first_reading=0
seconed_reaging = 0
count=0
word=0
Sql_Temp=0
conn = sqlite3.connect("Test_List.sqlite")
cur=conn.cursor()
#conn.execute("create table TempTest(temp, location)")
#first_reading =bus.read_byte_data(SLAVE_ADDRESS,register_read)
#print(first_reading)


    

class Command:
    def __init__(self):
        importlib.reload(Insert)
        self.requester=Insert.FusionTablesAPIRunner()
        self.requester.initialize()
    
    
    def Sql_Return(self,sql):
        print(sql)#温度の値渡し成功
        print("Sql_Return")
        return sql
    
    def R_Read(self,read_flag):
        reading=0
        if read_flag=='test':
            reading=0
            second_reading = 0
            time.sleep(0.1)
            test=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,4)
            test_list=[]
            for i in range(4):
                test_list,insert(i,chr(test[i]))
            test_mes=''.join(test_list)
            print(test_mes)
            
        if read_flag=='ad':
            msr=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,7)
            print(msr)
            msr_list=[]
            for i in range(7):
                msr_list.insert(i,chr(msr[i]))
            msr_mes=''.join(msr_list)
            print(msr_mes)
            
            
            
        if read_flag=='r':
            temp=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,11)
            temp_list=[]
            print(temp)
            for i in range(5,11):
                temp_list.insert(i,chr(temp[i]))
            temp_mes=''.join(temp_list)
            print(temp_mes)
            if temp[10] is not 0:
                temp_num=float(temp_mes)
            
                Sql_Temp=temp_num
                #print(temp_num)
                print("huga")
                today = datetime.datetime.today()
                #SQL文をそのまま渡す
                sql="INSERT INTO %s (Device_ID, TimeStamp, Temperature) values(%s,'%s',%s)" % (tableid,"001",today,temp_num)
                print(sql)
                print(type(sql))
                #Command().Sql_Return(sql)#SQL文をリターンするための値渡しができてるやん！
                
                print("Insert_Sql_Temp")
                #importlib.reload(Insert)
                
                #self.requester.query(sql,is_write_response=True)#インサート実行
                self.requester.query(sql)#インサート実行
                
                print("hoge")
            else :
                read_flag='r'
                importlib.reload(Read)
                Command().Read(read_flag)
            #Insert.FusionTablesAPIRunner().insert()#この書き方が、多分おかしい。
            #importlib.reload(Insert)
            
            #print("TEMPdone")
            #return Sql_Temp
            #return temp_num
            
            #return temp_num
            #return temp_num
            #return temp_num
            #now=str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            #conn.execute("insert into TempTest values('"+str(temp_mes)+"','"+now+"')")
            #cur.execute("select*from temptest")
            #for row in cur:
            #    print(str(row[0])+","+str(row[1]))
            #cur.close()
            
            
            #importlib.reload(Insert)
            
            """run = Insert.FusionTablesAPIRunner()
            
            run.initialize()
            run.insert()"""
            #Insert.Insertfunction()#外部のInsertを呼び出す。
            
        if read_flag=='else':
            else_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS)
            print(else_reading)
        return read_flag


    def Task_Command(self):
        
        command = 0
            
        command = input("Enter command:read-read data,test-send Test ")#コマンド入力
        if command == 'measure':#AD変換
            
                
                print("Measure")
                
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x4d,[0x65,0x61,0x73,0x75,0x72,0x65])
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x18,0x16])
                read_flag='ad'
                time.sleep(1.0)
                Command().R_Read(read_flag)
            
             
        elif command == 'r':
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
                read_flag='r'
                Command().R_Read(read_flag)
                
        elif command == 'test':
                test = 0    
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
                send_flag=True    
                read_flag='test'
                R_Read(read_flag)
                
        elif command =='read':
                cur.execute("select*from temptest")
                for row in cur:
                    print(str(row[0])+","+str(row[1]))
                
                
        elif command =='erase':
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x00,[0x00,0x00,0x00])
                time.sleep(1)
                print("erased")
                
        elif command =='uname':
                time.sleep(0.1)
                print(bus.read_word_data(SLAVE_ADDRESS,0x0f))
        
        elif command =='wait_read':
                Wait(read_flag)
                
        elif command =='wait_send':
                Wait(send_flag)
       
#while __name__=="__main__":
#while __name__=="__main__":
while True:
    Command().Task_Command()

