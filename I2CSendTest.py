#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
from enum import IntEnum

TaskName=['Init','Wait','ReadStart','ReadWait','ReadEnd','SendWait']


bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x0e#マイコンのi2Cアドレス、ここは絶対に変えない。
register_read = 0x1d#読み込み用アドレス
register_write= 0x1c#書き込み用アドレス

read_flag=False
send_flag=False
Read_Wait_Flag =False
Send_Wait_Flag =False
#def Read_CallBack:

def Task_Send():
    TaskSendNo = TaskName[5]
    if TaskSendNo==TaskName[5]:
        if send_flag is True:
            TaskSendNo is None
            TaskSendNo = TaskName[1]
            print(TaskNo)
            time.sleep(1)
"""
def Task_Read():
    TaskNo = TaskName[0]
    #print(TaskNo)
    if TaskNo == TaskName[0]:
        TaskNo = 0
        TaskNo1 = TaskName[1]#Wait
        print(TaskNo1)
        time.sleep(1)
    if TaskNo1==TaskName[1]:
        TaskNo1 is None
        TaskNo2 = TaskName[2]#ReadStart
        R_Read()
        print(TaskNo2)
        time.sleep(1)    
    if TaskNo2==TaskName[2]:
        TaskNo2 is None
        TaskNo3 = TaskName[3]#ReadWait
        print(TaskNo3)
        time.sleep(1)
        if TaskNo3==TaskName[3]:
            print(TaskNo3)
            if read_flag is True:
                TaskNo3 is None
                TaskNo4 = TaskName[4]#ReadEnd
                print(TaskNo4)
                time.sleep(1)
                if TaskNo4==TaskName[4]:
                    TaskNo4 is None
                    TaskNo5 = TaskName[5]#SendWait
                    Task_Command()
                    print(TaskNo5)
                    time.sleep(1)
            else:
                TaskNo2 = TaskName[2]
    else:
        TaskNo = TaskName[1]
        print('hoge')
        time.sleep(1)
"""

def R_Read():
    Wait()
    reading=int(bus.read_byte_data(SLAVE_ADDRESS,register_write))#指定されたアドレスのデータを１バイト読み取る
    
    if reading != 0:
        #Wait()
        print(reading)
        #Wait()
        Read_CallBack()
    elif reading == 0:
        
        #Wait()
        Read_CallBack()
        
    
def Wait():
    time.sleep(1.5)
    #print("address_byte")
    #read = int(bus.read_byte(SLAVE_ADDRESS))
    #print(read)
    #print("i2c")
    #print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_read))
    #print("byte")
    #print(bus.read_byte_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_byte_data(SLAVE_ADDRESS,register_read))
    #print("word")
    #print(bus.read_word_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_word_data(SLAVE_ADDRESS,register_read))

def Read_CallBack():
    read_flag=True
    R_Read()
    
def Send_CallBack():
    send_flag=True
    print('send')

#read = int(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,10))
#bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
#while read_flag is False:
    
    #bus.write_i2c_block_data(0x0e,0x1d,ord("1"))
    #print("初期化")
    #R_Read()
    #bus.write_i2c_block_data(0x0e,register_write,[0x13])
    #print(bus.read_i2c_block_data(0x0e,0x01,7))
    #R_Read()
    #bus.write_byte_data(SLAVE_ADDRESS,register_write,ord("1"))
    #print("初期化終わり")
def Task_Command():
    #if send_flag is True:
    #    Read()
    #else:
        
        command = input("Enter command: ad-pushAD, re-request, ping-ping,b12-bc:")#コマンド入力
        if command == 'measure':#AD変換
        
            time.sleep(1)
            print("ad")
            print("0x14=20を送る")
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
        
         #とりあえず石川さんのコマンドをそのまま
         #リクエス
        elif command == 'r':
            #bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
            #bus.write_i2c_block_data(0x0e,register_write,ord('a'))
            #bus.write_word_data(SLAVE_ADDRESS,register_write,ord("r"))
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x11,[0x18,0x16])
            #R_Read()
        elif command == 'test':
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
            Task_Send()
            Send_CallBack()
            Wait()
            R_Read()
        elif command =='read':
            #reading = 0
            #Task_Read()
            R_Read()
            Read_CallBack()
            
        elif command =='erase':
            bus.write_i2c_block_data(0x0e,0x00,[0x00,0x00])
            print("erased")
        elif command =='wait':
            if send_flag is True:
                R_Read()
            else :
                time.sleep(5)
        #time.sleep(1)
    #break;
#while read_flag is True:
#    print("read_mode")
#    print(int(bus.read_byte_data(SLAVE_ADDRESS,register_write)))
#    break;

while True:
    
    if read_flag is True:
        R_Read()
    else:
        Task_Command()
        
        #Task_Read()

