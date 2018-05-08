import smbus
import time
import sys
import RPi.GPIO as GPIO
bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

SLAVE_ADDRESS = 0x0e
reading = int(bus.read_byte(SLAVE_ADDRESS))

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    print(reading)

while True:
    request_reading()
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command == 's' and reading == 0:
        bus.write_byte(SLAVE_ADDRESS, ord('1'))
        print("send")
        GPIO.output(26,1)
    elif command == 'r' and reading ==0:
        print("reading is none")
    elif command == 'r' and reading != 0:
        #bus.write_byte(SLAVE_ADDRESS,ord('1'))
        print("reading is full")
        GPIO.output(4,1)
    elif command == 'end':
        sys.exit();
    elif reading != 0:
        bus.write_byte(SLAVE_ADDRESS,ord('1'))
        