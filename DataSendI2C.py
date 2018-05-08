import smbus
import time
import sys
bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x0e
reading = int(bus.read_byte(SLAVE_ADDRESS))

def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    print(reading)

while True:
    #request_reading()
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command == 's':
        bus.write_byte(SLAVE_ADDRESS, ord('1'))
        print("send")
    elif command == 'r' and reading ==0:
        request_reading()
        print("reading is none")
    elif command == 'r' and reading != 0:
        request_reading()
        print("reading is full")
    elif command == 'end':
        sys.exit();
    elif command =='stop':
        
    elif reading != 0:
        bus.write_byte(SLAVE_ADDRESS,ord('1'))
    