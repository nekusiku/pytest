#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
from enum import IntEnum
T=0x54
E=0x45
S=0x53
word=T
def wordset(word):
    if wordset==T:
        wordset=T+E
        print(wordset)
        
while True:
    wordset=T
    wordset(wordset)