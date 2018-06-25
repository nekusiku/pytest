#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

bus = smbus.SMBus(1)

while True:
    #read = int(bus.read_byte_data(0x0e,0x1c))
    #print (read)
    send = bus.write_block_data(0x0e,0x21,[0x13,0x14,0x15])
    print ("send")
    time.sleep(1)
    
    