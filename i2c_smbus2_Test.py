#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
import smbus2 


bus = smbus.SMBus(1)
b=bus.read_byte_data(0x16,0)
print(b)
