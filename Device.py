#!/usr/bin/python
# -*- code utf 8 -*-
import RPi.GPIO as GPIO
import time
import smbs
import serial
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.IN)
GPIO.output(3,1)
GPIO.output(5,0)