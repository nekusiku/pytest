#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(4,0)
GPIO.output(26,0)
SLAVE_ADDRESS = 0x0e
register_SLAVE = 0x00

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    print(reading)
    
reading = int(bus.read_byte(SLAVE_ADDRESS))>>10

while True:
    GPIO.cleanup()
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command == '1':
        bus.write_byte(SLAVE_ADDRESS, ord('1'))
        GPIO.output(4,1)
    elif command == 'r':
        request_reading()
        
    elif command == 't':
        bus.write_byte(SLAVE_ADDRESS, ord('t'))
        #request_reading()
        #bus.write_byte(SLAVE_ADDRESS,ord('t'))
        #print ("温度は"+str(bus.read_byte(SLAVE_ADDRESS,ord('t')))+"です")
        #print ("温度は"+reading<<10+"です")
        print ("温度は"+str(bus.read_byte(SLAVE_ADDRESS)>>2)+"です")

        """elif (bus.write_byte(SLAVE_ADDRESS, ord('t'))==1):
            request_reading()
            if(request_reading()==1):
                print(int(bus.read_byte(SLAVE_ADDRESS)))
                long read_word_data(int addr,char cmd)"""
    elif command =='end':
        bus.write_byte(SLAVE_ADDRESS, ord('e'))
        GPIO.cleanup()
        break;
        