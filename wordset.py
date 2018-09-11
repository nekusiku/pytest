#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys

T=0x54
E=0x45
S=0x53
test_list=[T,E,S,T]
print(test_list)
chr_test=[]
test_sum=0
for i in range (4):
    chr_test.insert(i,chr(test_list[i]))
    
    print(chr_test)
    #chr_test[i]=chr(test_list[i])
    
    #test_sum+=test_list[i]
    #print(test_sum)
chr=''.join(chr_test)
print(chr)
