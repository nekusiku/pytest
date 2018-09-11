#!/usr/bin/env python
#-*- coding: utf-8 -*-
import serial
import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
import sqlite3

test_temp=str("test_temp=21.15")

print(test_temp)

#このデータをデータベースに入れたい。

