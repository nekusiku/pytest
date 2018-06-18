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
#def Read_CallBack:

def Task():
    TaskNo= TaskName[0]#Init
    print(TaskNo)
    if TaskNo == TaskName[0]:
        TaskNo = TaskName[1]#Wait
        print(TaskNo)
        time.sleep(1)
    if TaskNo==TaskName[1]:
        TaskNo = TaskName[2]#ReadStart
        print(TaskNo)
        time.sleep(1)
    if TaskNo==TaskName[2]:
        TaskNo = TaskName[3]#ReadWait
        print(TaskNo)
        time.sleep(1)
    if TaskNo==TaskName[3]:
        if read_flag is True:
            TaskNo = TaskName[4]#ReadEnd
            print(TaskNo)
            time.sleep(1)
    if TaskNo==TaskName[4]:
        TaskNo = TaskName[5]#SendWait
        Task_Command()
        print(TaskNo)
        time.sleep(1)
    if TaskNo==TaskName[5]:
        if send_flag is True:
            TaskNo = TaskName[1]
            print(TaskNo)
            time.sleep(1)
    else:
        TaskNo = TaskName[1]
        print('hoge')
        time.sleep(1)
        

def R_Read():
    reading=int(bus.read_byte_data(SLAVE_ADDRESS,register_write))#指定されたアドレスのデータを１バイト読み取る
    print(reading)
    Read_CallBack()

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
    
def D_Read():
    d_read=str(bus.read_byte(SLAVE_ADDRESS).decode())
    print(d_read)
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
        Send_CallBack()
    elif command =='read':
        R_Read()
        Read_CallBack()
    elif command =='erase':
        bus.write_i2c_block_data(0x0e,0x00,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        print("erased")
    elif command =='wait':
        if send_flag is True:
            R_Read()
        else :
            time.sleep(5)
    time.sleep(1)
    #break;
#while read_flag is True:
#    print("read_mode")
#    print(int(bus.read_byte_data(SLAVE_ADDRESS,register_write)))
#    break;

while True:
    Task_Command()
    #Task()
