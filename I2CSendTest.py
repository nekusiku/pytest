#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x0e#マイコンのi2Cアドレス、ここは絶対に変えない。
register_read = 0x1d#読み込み用アドレス
register_write= 0x1c#書き込み用アドレス

def R_Read():
    #reading=int(bus.read_byte_data(SLAVE_ADDRESS,register_read))#指定されたアドレスのデータを１バイト読み取る
    #print(reading)
    read = int(bus.read_byte(SLAVE_ADDRESS))
    print(read)
    print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_write))
    print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_read))
    print("byte")
    print(bus.read_byte_data(SLAVE_ADDRESS,register_write))
    print(bus.read_byte_data(SLAVE_ADDRESS,register_read))
    print("word")
    print(bus.read_word_data(SLAVE_ADDRESS,register_write))
    print(bus.read_word_data(SLAVE_ADDRESS,register_read))
    #print(bus.read_block_data(SLAVE_ADDRESS,register_read))ここをいじるとクラッシュが発生するためいじらないこと。
def D_Read():
    d_read=str(bus.read_byte(SLAVE_ADDRESS).decode())
    print(d_read)
#read = int(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,10))
#bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
while True:
    #bus.write_i2c_block_data(0x0e,0x1d,ord("1"))
    #print("初期化")
    #R_Read()
    #bus.write_i2c_block_data(0x0e,register_write,[0x13])
    #print(bus.read_i2c_block_data(0x0e,0x01,7))
    #R_Read()
    #bus.write_byte_data(SLAVE_ADDRESS,register_write,ord("1"))
    #print("初期化終わり")

    command = input("Enter command: ad-pushAD, re-request, ping-ping,b12-bc:")#コマンド入力
    if command == 'measure':#AD変換
        
        R_Read()
        print("ad")
        print("0x14=20を送る")
        #bus.write_i2c_block_data(0x0e,register_write,[0x17,0x12,0x19])
        #bus.write_word_data(SLAVE_ADDRESS,register_write,ord("1"))
        #bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x13])
        #bus.write_word_data(0x0e,register_write,0x14)
        #bus.write_block_data(0x0,register_write,0x14)
        #bus.write_i2c_block_data(0x0e,register_write,[0x17])
        time.sleep(1)
        R_Read()
     #とりあえず石川さんのコマンドをそのまま
     #リクエス
    elif command == 'r':
        #bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
        #bus.write_i2c_block_data(0x0e,register_write,ord('a'))
        #bus.write_word_data(SLAVE_ADDRESS,register_write,ord("r"))
        bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x11,0x18,0x16])
        time.sleep(1)
        R_Read()
        time.sleep(1)
        R_Read()
    elif command == 'test':
        #bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00])
        bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x13])
        print("sended")
        #R_Read()
        #bus.write_i2c_block_data(0x0e,register_write,[0x13,0x14,0x15])
        #print('Test')
        
        #bus.write_i2c_block_data(0x0e,register_write,[0x13])
       
        #print(bus.read_i2c_block_data(0x0e,register_write,3))
        #print(0x18)
        #time.sleep(1)
        #R_Read()
        print("end")
    elif command =='repeat':
        bus.write_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00])
        R_Read()
        time.sleep(1)
        R_Read()
        time.sleep(1)
        R_Read()
    time.sleep(1)
    #指定されたバイト数のデータを読み取る、この読み取り部分
"""
while True:
    a = [0x13,0xff,0xff]
    bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x13,0xff,0xff])
    #bus.write_byte(SLAVE_ADDRESS,1)
    time.sleep(1)
    #for num in range (0,10):
    #bus.write_i2c_block_data(SLAVE_ADDRESS,)
    #for num in range(0,10):
    if(bus.read_i2c_block_data(SLAVE_ADDRESS,register_read,10)!=0):
        bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x13,0xff,0xff])
        print(bus.read_i2c_block_data(0x0e,register_read,10))
        
        print(bus.read_byte(SLAVE_ADDRESS))
        print(bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[0x13,0xff,0xff]))
        
        R_Read()
        time.sleep(2)
"""
