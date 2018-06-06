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
reading = int(bus.read_byte_data(SLAVE_ADDRESS,0x1c))

def request_reading():
    reading = int(bus.read_byte_data(SLAVE_ADDRESS,0x1c))
    print(reading)

    
while True:
    request_reading()
    bus.write_byte_data(SLAVE_ADDRESS,0x1d,ord('1'))
    time.sleep(1)
    if(request_reading()!=0):
        #GPIO.output(4,1)
        #GPIO.output(26,0)
        #time.sleep(1)
        print("read")
        bus.write_byte_data(SLAVE_ADDRESS,0x1d,ord('1'))
        if(bus.write_byte_data(SLAVE_ADDRESS,0x1d,ord('1'))!=0):
            time.sleep(1)
            #GPIO.output(4,0)
            #GPIO.output(26,1)
            time.sleep(1)
            print("send")
    