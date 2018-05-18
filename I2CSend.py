#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x0e
register_SLAVE = 0x00
#while True:
#bus.write_byte_data(SLAVE_ADDRESS,register_SLAVE,ord())
bus.write_byte_data(SLAVE_ADDRESS,register_SLAVE,0x13)
time.sleep(1)
print(bus.write_byte_data(SLAVE_ADDRESS,register_SLAVE,0x13))
if(bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE)!=0):
        time.sleep(1)
        print(bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE))