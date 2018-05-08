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

while (reading!=0):
    request_reading()
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    
    if command =='s':
        print("stop")
    
    elif command == 'r':
        #bus.write_byte(SLAVE_ADDRESS,ord('1'))
        print("reading is full")
        GPIO.output(4,1)
    
    elif command == 'end':
        GPIO.cleanup()
        sys.exit()
    
    else:
        bus.write_byte(SLAVE_ADDRESS,ord('1'))

while (reading==0):
    command = input("Enter command: 1-Toggle LED, r-read A0:")

    if command == 's':
        bus.write_byte(SLAVE_ADDRESS, ord('1'))
        print("send")
        GPIO.output(26,1)
    
    elif command == 'r':
        print("reading is none")
        
    elif command == 'end':
        GPIO.cleanup()
        sys.exit()