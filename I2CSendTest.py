#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smbus
import time
import RPi.GPIO as GPIO
import serial
import sys
from enum import IntEnum

TaskName=['Init','Wait','ReadStart','ReadWait','ReadEnd','SendWait']

count = 0
bus = smbus.SMBus(1)#i2Cの設定
MICON_ADDRESS = 0x2c#マイコンのi2Cアドレス、ここでのアドレスはマイコンだと左に１ビットずれた状態になる。
SLAVE_ADDRESS = MICON_ADDRESS>>1#ややこしくなるので、こっちでも同じ数字で設定して、関数でずらし問題がないようにする。

print(hex(MICON_ADDRESS))
print(hex(SLAVE_ADDRESS))
register_read = 0x2c#読み込み用デバイスレジスタアドレス
register_write= 0x1e#書き込み用デバイスレジスタアドレス
_Command = 0x00
_Data=0x40
#_Config =0b
send_flag=False
read_flag=False

Read_Wait_Flag =False
Send_Wait_Flag =False
#def Read_CallBack:
first_reading=0
seconed_reaging = 0
count=0
word=0
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
def wordset(wordset):
    if wordset==T:
        wordset=T
    
    
def R_Read():
    #time.sleep(0.01)
    
    first_reading = 0
    second_reading = 0
    #reading_list
    
    #    reading=0
        #time.sleep(5)
    #try :
            #reading_block=bus.read_block_data(SLAVE_ADDRESS,register_read)
    #reading=bus.read_i2c_block_data(SLAVE_ADDRESS,0xfe934)
    #reading=bus.read_i2c_block_data(SLAVE_ADDRESS,_Data,3)
    #for count in range(5):
    #first_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,0x2c,5)
##    for count in range(5):
    second_reading=bus.read_byte_data(SLAVE_ADDRESS,0x2c)
    print(second_reading)
    
    #print("Count:")
    #print(count)
    """if second_reading==0xff:
        read_flag = False
        print(first_reading)
        #count=count+1
        #Read_CallBack(read_flag)
        print("huga")"""
    if second_reading==0x54:
        print(first_reading)
        print(second_reading)
        print("0x54==T")
        T=(chr(second_reading))
        print(T)
        wordset=T
        read_flag=True
        Read_CallBack(read_flag)
    if second_reading==0x65:
        print(first_reading)
        #print(chr(second_reading))
        print("0x65=e")
        read_flag=True
        Read_CallBack(read_flag)
    if second_reading==0x73:
        print(first_reading)
        #print(chr(second_reading))
        print("0x73=s")
        read_flag=True
        Read_CallBack(read_flag)
    if second_reading==0x74:
        print(first_reading)
        print(chr(second_reading))
        print("0x74=t")
        read_flag=True
        Read_CallBack(read_flag)
    else:
        #read_flag=True
        #count=count+1
        #print(hex(first_reading))
        #print(chr(first_reading))
        #print((first_reading))
        print(second_reading)
        print(chr(second_reading))
        #print(chr(second_reading))
        #print(hex(second_reading))
        #Read_CallBack(read_flag)
        print("hoge")
    """if first_reading==0x54 :
        print(hex(first_reading))
        print(chr(first_reading))
        #print(hex(reading))  
    elif first_reading==0x45:
        print(hex(first_reading))
        print(chr(first_reading))
    elif first_reading==0x53:
        print(hex(first_reading))
        print(chr(first_reading))
    else:
        print(first_reading)
        print(chr(first_reading))
        print(hex(first_reading))
    #reading = i2cset -y 1 SLAVE_ADDRESS
    """
        #time.sleep(0.1)
        #reading += reading
            #reading =bus.read_byte(SLAVE_ADDRESS)
            #reading=bus.read_word_data(SLAVE_ADDRESS,register_read)#指定されたアドレスのデータを１バイト読み取る
    #except Exception:
    #    print("受信できませんでした")
            
    
        #count = count+1
        #print(count)
        #print(ascii())
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
        print("read")
        
        R_Read()
        #Wait(read_flag)
    elif read_flag==False:
        print("can not read")
       
    
def Send_CallBack(send_flag):
    if send_flag == True:
        send_flag=True
        print('send')
        #Wait(send_flag)
        #for i in range(0,5):
        #time.sleep(0.5)
        R_Read()
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
        #bus.write_i2c_block_data(SLAVE_ADDRESS,register_write,[1])
        command = 0
        
        command = input("Enter command:read-read data,test-send Test ")#コマンド入力
        if command == 'measure':#AD変換
        
            
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
            
            test = 0
            try:
                
                bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x2c,[hex("T")])
                #bus.write_i2c_block_data(SLAVE_ADDRESS,0x54,[0x45,0x53,0x54])
                send_flag = True
                
                Send_CallBack(send_flag)
                
            except Exception:
                print("送信できませんでした")
                send_flag = False
                Send_CallBack(send_flag)

            
                
            
            #read_write = bus.read_i2c_block_data(SLAVE_ADDRESS,register_write)
            #print(read_write)
            #Task_Send()
            #read_read = bus.read_i2c_block_data(SLAVE_ADDRESS,register_read)
            #print(read_read)
           #Send_CallBack()
        elif command =='read':
            
            
            R_Read()
            
        elif command =='erase':
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x00,[0x00])
            time.sleep(1)
            print("erased")
        elif command =='uname':
            time.sleep(0.1)
            print(bus.read_word_data(SLAVE_ADDRESS,0x0f))
        elif command =='wait_read':
            Wait(read_flag)
        elif command =='wait_send':
            Wait(send_flag)
        """elif command =='combine':
            Word=T+E+S+T
            print(Word)"""
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
    #    breakest
    
    #    R_Read()
    #elif read_flag == False:
        #time.sleep(0.01)
    Task_Command()
    
    
        #    break
            #Task_Read()
    
