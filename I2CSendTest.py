#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x0e#マイコンのi2Cアドレス、ここは絶対に変えない。
register_read = 0x1c#読み込み用アドレス(マイコンの書き込み)
register_write= 0x1d#書き込み用アドレス(マイコンの読み込み)

def R_Read():
    reading=int(bus.read_byte(SLAVE_ADDRESS))#指定されたアドレスのデータを１バイト読み取る
    print(reading)

#read = int(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,10))
while True:

    command = input("Enter command: ad-pushAD, re-request, ping-ping,b12-bc:")#コマンド入力
    if command == 'ad':#AD変換
        bus.write_i2c_block_data(0x0e,register_write,[0x17])
        time.sleep(1)
        print("ad")
        R_Read()
        bus.write_i2c_block_data(0x0e,register_write,[0x20])
        time.sleep(1)
        R_Read()
        bus.write_i2c_block_data(0x0e,register_write,[0x5A])
        time.sleep(1)
        R_Read()
    #とりあえず石川さんのコマンドをそのまま
    elif command == 're':
        bus.write_i2c_block_data(0x0e,register_write,[0x13])
        print(bus.read_i2c_block_data(0x0e,register_read,5))
        R_Read()
        time.sleep(1)
        bus.write_i2c_block_data(0x0e,register_write,[0xff])
        time.sleep(1)
        R_Read()
        bus.write_i2c_block_data(0x0e,register_write,[0xff])
        time.sleep(1)
        R_Read()
        
    elif command == 'ping':
        bus.write_i2c_block_data(0x0e,register_write,[0x17,0x10,0x5A])
        R_Read()
    elif command == 'b12':
        bus.write_i2c_block_data(0x0e,register_write,[0x17,0x30,0x5A])
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
