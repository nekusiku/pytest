#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(4,0)
GPIO.output(26,0)
SLAVE_ADDRESS = 0x0e
register_SLAVE = 0x00

def request_reading():
    reading = int(bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE))
    print(reading)
    
def request_readingstr():
    reading_rg = str(bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE))
    print(reading_rg)

def request_read_word():
    reading_word = str(bus.read_word_data(SLAVE_ADDRESS,register_SLAVE))
    print(reading_word)




while True:
    GPIO.cleanup()
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    reading=None
    if command == '1':
        bus.write_byte(SLAVE_ADDRESS,'1')
        GPIO.output(4,1)
    elif command == 'r':
        bus.write_byte(SLAVE_ADDRESS,ord('r'))
        #request_reading()
        #request_read_word()
        #request_readingstr()
        print(bus.read_byte(SLAVE_ADDRESS))
        bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE)
        
    elif command == 't':
        
        #bus.write_byte(SLAVE_ADDRESS,ord("1"))
        #bus.write_byte(SLAVE_ADDRESS,ord('t'))
        t = 0x14
        bus.write_byte_data(SLAVE_ADDRESS,register_SLAVE,1)
        bus.write_word_data(SLAVE_ADDRESS,register_SLAVE,0xFF)
        bus.write_word_data(SLAVE_ADDRESS,register_SLAVE,0xFF)
        #bus.write_i2cblock_data(SLAVE_ADDRESS,ord(s[0]),ord(s[1:]))
        #request_reading()
        #bus.write_byte(SLAVE_ADDRESS,ord('t'))
        #print ("温度は"+str(bus.read_byte(SLAVE_ADDRESS,ord('t')))+"です")
        #print ("温度は"+reading<<10+"です")
        if bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE)!=0:
            time.sleep(1)
            print ("温度は"+str(bus.read_byte_data(SLAVE_ADDRESS,register_SLAVE))+"℃です")
            print ("温度は"+str(bus.read_byte(SLAVE_ADDRESS))+"℃です")
            print ("温度は"+str(bus.read_word_data(SLAVE_ADDRESS,register_SLAVE)>>8)+"℃です")
            #print (str(bus.write_word_data(SLAVE_ADDRESS,register_SLAVE,ord('t'))))
        """elif (bus.write_byte(SLAVE_ADDRESS, ord('t'))==1):
            request_reading()
            if(request_reading()==1):
                print(int(bus.read_byte(SLAVE_ADDRESS)))
                long read_word_data(int addr,char cmd)"""
        
    elif command =='end':
        bus.write_byte(SLAVE_ADDRESS, ord('e'))
        GPIO.cleanup()
        break;
    elif command =="w":
        bus.write_byte(SLAVE_ADDRESS, ord('2'))
        if bus.read_byte(SLAVE_ADDRESS)!=0:
            request_read_word()
            request_readingstr()
    elif command =="b":
        bus.write_byte(SLAVE_ADDRESS, ord('3'))
        if bus.read_byte(SLAVE_ADDRESS)is not None:
            request_read_word()
            request_readingstr()
    elif command =="t":
        bus.write_byte(SLAVE_ADDRESS,ord('4'))
        