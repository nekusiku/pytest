#!/usr/bin/python
# -*- code utf 8 -*-
import RPi.GPIO as GPIO
import time
import sys
import smbus
import serial
from time import sleep
GPIO.setmode(GPIO.BOARD)
def read_BH1020():
    word_data = bus.read_word_data(address_BH1020,register_BH1020)
    data = (word_data & 0xff00)>>8 | (word_data&0xff)<<8
    data = data>>3
    if data & 0x1000 == 0:
        temperature = data*0.0625
    else: 
        temperature = ( (~data&0x1fff) + 1)*-0.0625
    return temperature

bus = smbus.SMBus(1)
address_BH1020 = 0x0e
register_BH1020= 0x00

try:
    while True:
        inputValue = read_BH1020()
        print(inputValue)
        sleep(0.5)

except KeyboardInterrupt:
    pass
