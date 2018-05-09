
import smbus
import time
import RPi.GPIO as GPIO
bus = smbus.SMBus(1)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

GPIO.output(4,0)
GPIO.output(26,0)

SLAVE_ADDRESS = 0x0e

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    print(reading)

while True:
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command == '1':
        bus.write_byte(SLAVE_ADDRESS, ord('1'))
        GPIO.output(4,1)
    elif command == 'r':
        request_reading()
    elif command == 't':
        request_reading();