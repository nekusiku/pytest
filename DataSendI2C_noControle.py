import smbus
import time
import sys
import RPi.GPIO as GPIO
bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(4,0)
GPIO.output(26,0)
SLAVE_ADDRESS = 0x0e
reading = int(bus.read_byte(SLAVE_ADDRESS))

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    print(reading)

    
while True:
    request_reading()
    GPIO.output(4,1)
    GPIO.output(26,0)
    time.sleep(1)
    
    if(reading !=0):
        print("read")
        bus.write_byte(SLAVE_ADDRESS,ord('1'))
        time.sleep(1)
        GPIO.output(4,0)
        GPIO.output(26,1)
        time.sleep(1)
        print("replyed")