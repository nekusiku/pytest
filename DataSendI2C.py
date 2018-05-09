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
#sending = int(bus.write_byte(SLAVE_ADDRESS))
#def send():
#    bus.write_byte(SLAVE_ADDRESS('1'))
def request_reading():
    reading = int(bus.read_byte(SLAVE_ADDRESS))
    time.sleep(1)
    print("reading,byte_is")
    time.sleep(1)
    print(reading)

    
while (reading!=0):
    
    request_reading()
    print("recieve-mode")
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command =='s':
        GPIO.cleanup()
        print("stop")
        break
    elif command == 'r':
        request_reading()
        print("reading is full")
        
        GPIO.output(4,1)
        GPIO.output(26,0)
        time.sleep(1)
        bus.write_byte(SLAVE_ADDRESS,ord('1'))
        time.sleep(1)
        GPIO.output(4,0)
        GPIO.output(26,1)
    elif command == 'end':
        GPIO.cleanup()
        break
    
    else:
        bus.write_byte(SLAVE_ADDRESS,ord('1'))
    
while(reading==0):
    #GPIO.cleanup()
    request_reading()
    print("send_mode")
    command = input("Enter command: 1-Toggle LED, r-read A0:")
    if command == 's' :
        time.sleep(1)
        #send() 
        #bus.write_byte(SLAVE_ADDRESS, ord('1'))
        print("send")
        GPIO.output(26,1)
    elif command == 'r' and reading == 0:
        request_reading()
        print("reading is none")
    elif command == 'end':
        GPIO.cleanup()
        break
