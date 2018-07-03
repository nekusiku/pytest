#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
from enum import IntEnum

read_list=[0x54,0x45,0x53,0x54]
T=(chr(read_list[0]))
E=(chr(read_list[1]))
S=(chr(read_list[2]))
print(T+E+S+T)