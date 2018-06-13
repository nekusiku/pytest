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

while True:
    bus.write_byte_data(SLAVE_ADDRESS,register_write,ord("1"))
    R_Read()
    time.sleep(1)
    