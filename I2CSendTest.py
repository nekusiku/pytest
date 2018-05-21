#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x0e#マイコンのi2Cアドレス、ここは絶対に変えない。
register_SLAVE = 16#温度センサにつなげるアドレス


def R_Read():
    reading=int(bus.read_byte(SLAVE_ADDRESS))#指定されたアドレスのデータを１バイト読み取る
    print(reading)

#read = int(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,10))
"""while True:

    command = input("Enter command: ad-pushAD, re-request, ping-ping,b12-bc:")#コマンド入力
    if command == 'ad':#AD変換
        bus.write_i2c_block_data(0x0e,0x17,[0x20,0x5A])
        time.sleep(1)
        print("ad")
    とりあえず石川さんのコマンドをそのまま
    elif command == 're':
        bus.write_i2c_block_data(0x0e,0x13,[0xFF,0xFF])
    elif command == 'ping':
        bus.write_i2c_block_data(0x0e,0x17,[0x10,0x5A])
    elif command == 'b12':
        bus.write_i2c_block_data(0x0e,0x17,[0x30,0x5A])
        
    time.sleep(1)
    #指定されたバイト数のデータを読み取る、この読み取り部分
"""
for num in range (1,10):
    #bus.write_i2c_block_data(SLAVE_ADDRESS,)
    print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,1))
    
    #R_Read()
        
