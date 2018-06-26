#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
from enum import IntEnum

TaskName=['Init','Wait','ReadStart','ReadWait','ReadEnd','SendWait']


bus = smbus.SMBus(1)#i2Cの設定
SLAVE_ADDRESS = 0x0e#マイコンのi2Cアドレス、ここは絶対に変えない。
register_read = 0x1d#読み込み用アドレス
register_write= 0x1b#書き込み用アドレス

send_flag=False
read_flag=False

Read_Wait_Flag =False
Send_Wait_Flag =False
#def Read_CallBack:
first_reading=0
seconed_reaging = 0

#first_reading =bus.read_byte_data(SLAVE_ADDRESS,register_read)
#print(first_reading)
"""
def Task_Send():
    TaskSendNo = TaskName[5]
    if TaskSendNo==TaskName[5]:
        if send_flag == True:
            TaskSendNo == None
            TaskSendNo = TaskName[1]
            print(TaskNo)
            time.sleep(1)
            Wait(Send_flag)"""
"""
def Task_Read():
    TaskNo = TaskName[0]
    #print(TaskNo)
    if TaskNo == TaskName[0]:
        TaskNo = 0
        TaskNo1 = TaskName[1]#Wait
        print(TaskNo1)
        time.sleep(1)
    if TaskNo1==TaskName[1]:
        TaskNo1 is None
        TaskNo2 = TaskName[2]#ReadStart
        R_Read()
        print(TaskNo2)
        time.sleep(1)    
    if TaskNo2==TaskName[2]:
        TaskNo2 is None
        TaskNo3 = TaskName[3]#ReadWait
        print(TaskNo3)
        time.sleep(1)
        if TaskNo3==TaskName[3]:
            print(TaskNo3)
            if read_flag is True:
                TaskNo3 is None
                TaskNo4 = TaskName[4]#ReadEnd
                print(TaskNo4)
                time.sleep(1)
                if TaskNo4==TaskName[4]:
                    TaskNo4 is None
                    TaskNo5 = TaskName[5]#SendWait
                    Task_Command()
                    print(TaskNo5)
                    time.sleep(1)
            else:
                TaskNo2 = TaskName[2]
    else:
        TaskNo = TaskName[1]
        print('hoge')
        time.sleep(1)
"""

def R_Read():
    
    count = 0
    while count < 5:
        reading=0
        #time.sleep(5)
        #second_reading=0
        #reading_block = 0
        try :
            #reading_block=bus.read_block_data(SLAVE_ADDRESS,register_read)
            reading=bus.read_word_data(SLAVE_ADDRESS,register_read)
            #reading =bus.read_byte(SLAVE_ADDRESS)
            #reading=bus.read_word_data(SLAVE_ADDRESS,register_read)#指定されたアドレスのデータを１バイト読み取る
        except Exception:
            print("受信できませんでした")
            break
            count = count -1
        count = count+1
        print(count)
        print(reading)
        #print(str(reading).encode.utf-8)
    
    #second_reading=int(bus.read_byte(SLAVE_ADDRESS))
    #print(second_reading)
    """if second_reading != first_reading:
        #Wait()
        print(second_reading)
        #Wait()
        #reading=0
        #Read_CallBack()
    elif second_reading == first_reading:
        print("none")
        #Wait()
        #Read_CallBack()"""


        

def Wait(send_flag):
    if send_flag==True and read_flag==False:
        print("sendTrue")
       
        #R_Read()
    else:
        print("none")
        
def Wait(read_flag):

    if read_flag==True and send_flag==False:
        print("readTrue")
        R_Read()
        
    else:
        print("none")
        
    #print("address_byte")
    #read = int(bus.read_byte(SLAVE_ADDRESS))
    #print(read)
    #print("i2c")
    #print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_i2c_block_data(SLAVE_ADDRESS,register_read))
    #print("byte")
    #print(bus.read_byte_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_byte_data(SLAVE_ADDRESS,register_read))
    #print("word")
    #print(bus.read_word_data(SLAVE_ADDRESS,register_write))
    #print(bus.read_word_data(SLAVE_ADDRESS,register_read))

def Read_CallBack(read_flag):
    if read_flag==True:
        print("can read")
        Wait(read_flag)
    elif read_flag==False:
        print("can not read")
       
    
def Send_CallBack(send_flag):
    if send_flag == True:
        send_flag=True
        print('send')
        #Wait(send_flag)
        #for i in range(0,5):
        #R_Read()
    elif send_flag == False:
        send_flag=False
        print('can not send')
#read = int(bus.read_i2c_block_data(SLAVE_ADDRESS,register_SLAVE,10))
#bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
#while read_flag is False:
    
    #bus.write_i2c_block_data(0x0e,0x1d,ord("1"))
    #print("初期化")
    #R_Read()
    #bus.write_i2c_block_data(0x0e,register_write,[0x13])
    #print(bus.read_i2c_block_data(0x0e,0x01,7))
    #R_Read()
    #bus.write_byte_data(SLAVE_ADDRESS,register_write,ord("1"))
    #print("初期化終わり")
def Task_Command():
    #if send_flag is True:
    #    Read()
    #else:
        command = 0
        command = input("Enter command:read-read data,test-send Test ")#コマンド入力
        if command == 'measure':#AD変換
        
            time.sleep(1)
            print("ad")
            print("0x14=20を送る")
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
        
         #とりあえず石川さんのコマンドをそのまま
         #リクエス
        elif command == 'r':
            #bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
            #bus.write_i2c_block_data(0x0e,register_write,ord('a'))
            #bus.write_word_data(SLAVE_ADDRESS,register_write,ord("r"))
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x11,[0x18,0x16])
            #R_Read()
        elif command == "test":
            bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[1])
            test = 0
            try:
                time.sleep(0.1)
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
                send_flag = True
                time.sleep(0.5)
                Send_CallBack(send_flag)
                
            except Exception:
                print("送信できませんでした")
                send_flag = False
                Send_CallBack(send_flag)

            time.sleep(1)
                
            
            #read_write = bus.read_i2c_block_data(SLAVE_ADDRESS,register_write)
            #print(read_write)
            #Task_Send()
            #read_read = bus.read_i2c_block_data(SLAVE_ADDRESS,register_read)
            #print(read_read)
           #Send_CallBack()
        elif command =='read':
            time.sleep(2)
            R_Read()
            
        elif command =='erase':
            bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[1])
            time.sleep(1)
            print("erased")
        elif command =='uname':
            time.sleep(0.1)
            print(bus.read_word_data(SLAVE_ADDRESS,0x0f))
        elif command =='wait_read':
            Wait(read_flag)
        elif command =='wait_send':
            Wait(send_flag)
"""if send_flag is True:
                R_Read()
            else :
                time.sleep(5)"""
        #time.sleep(1)
    #break;
#while read_flag is True:
#    print("read_mode")
#    print(int(bus.read_byte_data(SLAVE_ADDRESS,register_write)))
#    break;

while True:
    
    #if read_flag == True:
    #    break
    #    R_Read()
    #elif read_flag == False:
        Task_Command()
    #    break
        #Task_Read()

