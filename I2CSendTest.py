#!/usr/bin/env python
#-*- coding: utf-8 -*-
import serial
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
REGISTER_ADDRESS=0x13#マイコンのレジスタアドレス、仮で設定する。
print(hex(MICON_ADDRESS))
print(hex(SLAVE_ADDRESS))
print(hex(REGISTER_ADDRESS))
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
    
    
def R_Read(read_flag):
    #time.sleep(0.01)
    if read_flag=='test':
        first_reading = 0
        second_reading = 0
        time.sleep(0.1)
        second_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,4)
        #second_reading=bus.read_word_data(SLAVE_ADDRESS,0x2c)
        print(second_reading)
    
        #if count==0:
        read_0=second_reading[0]
        #print(read_0)
        read_1=(second_reading[1])
        #print(read_1)
        read_2=(second_reading[2])
        #print(read_2)
        read_3=(second_reading[3])
        #print(read_3)
        print(chr(read_0)+chr(read_1)+chr(read_2)+chr(read_3))
    if read_flag=='ad':
        ad_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,2)
        print(ad_reading)
    if read_flag=='r':
        r_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS,2)
        print(r_reading)
    if read_flag=='else':
        else_reading=bus.read_i2c_block_data(SLAVE_ADDRESS,REGISTER_ADDRESS)
        print(else_reading)
        #print(chr(second_reading))
##    time.sleep(0.01)
    #print("Count:")
    #print(count)
    
        #print(chr(second_reading))


def Read_CallBack(read_flag):
    if read_flag==True:
        print("True")
    elif read_flag=='T_True':
        print("readT")
        send_flag='T_True'
        Send_CallBack(send_flag)
        #R_Read()
        #Wait(read_flag)
    elif read_flag=='e_True':
        print("readE")
        send_flag="E_True"
    elif read_flag=='s_True':
        print("readE")
        send_flag="E_True"
    elif read_flag=='t_True':
        print("readt")
        send_flag="t_True"
    elif read_flag==False:
        print("can not read")
    #elif read_flag==True:
        
    
def Send_CallBack(send_flag):
    if send_flag == True:
        #bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
        send_flag=True
        print('send')
        #Wait(send_flag)
        #for i in range(0,5):
        #time.sleep(0.5)
        R_Read()
    elif send_flag == False:
        send_flag=False
        print('can not send')
    elif send_flag == 'T_True':
        
        bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
        read_flag='e_True'
        
        R_Read()
    elif send_flag == 'E_True':
        send_flag ='s_True'
        
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
            
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x11,[0x18,0x16])
            print("0x14=20を送る")
            read_flag='ad'
            R_Read(read_flag)
         #とりあえず石川さんのコマンドをそのまま
         #リクエス
    elif command == 'r':
            #bus.write_i2c_block_data(0x0e,register_write,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
            #bus.write_i2c_block_data(0x0e,register_write,ord('a'))
            #bus.write_word_data(SLAVE_ADDRESS,register_write,ord("r"))
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x17,[0x12,0x19])
            read_flag='r'
            R_Read(read_flag)
    elif command == 'test':
            
            test = 0
            
                
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x13,[0x14,0x15])
            #bus.write_i2c_block_data(SLAVE_ADDRESS,0x2c,)
            #bus.write_i2c_block_data(SLAVE_ADDRESS,0x54,[0x45,0x53,0x54])
            #send_flag ='T_True'
            send_flag=True    
            #Send_CallBack(send_flag)
            
                
            
            #read_write = bus.read_i2c_block_data(SLAVE_ADDRESS,register_write)
            #print(read_write)
            #Task_Send()
            #read_read = bus.read_i2c_block_data(SLAVE_ADDRESS,register_read)
            #print(read_read)
           #Send_CallBack()
            read_flag='test'
            R_Read(read_flag)
    elif command =='read':
            
            read_flag='else'
            R_Read(read_flag)
            
    elif command =='erase':
            bus.write_i2c_block_data(SLAVE_ADDRESS,0x00,[0x00,0x00,0x00])
            time.sleep(1)
            print("erased")
    elif command =='uname':
            time.sleep(0.1)
            print(bus.read_word_data(SLAVE_ADDRESS,0x0f))
    elif command =='wait_read':
            Wait(read_flag)
    elif command =='wait_send':
            Wait(send_flag)
       
while True:
    
    #if read_flag == True:
    #    breakest
    
    #    R_Read()
    #elif read_flag == False:
        #time.sleep(0.01)
    Task_Command()
    
    
        #    break
            #Task_Read()
    
