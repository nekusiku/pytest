#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x2c#マイコンのi2Cアドレス、ここは絶対に変えない。
register_read = 0x1d#読み込み用アドレス
register_write= 0x1c#書き込み用アドレス

i2cget -y 1 0x2c 0x2c