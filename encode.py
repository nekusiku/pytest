#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import sys
import codecs

#sys.stdout=coeecs.getwriter('utf_8')(sys.stdout)
#print u'これでいいのだ'

enc = 0x40
print (chr(enc))
bunkaino = 0xff
denatu=5
bitatari = denatu/bunkaino
print(bitatari)
x1=-40
x2=70
y1=1.9
y2=1.0
a=(y2-y1)/(x2-x1)
print("a=")
print(a)
x=25
b=1.9-0.3272
print("b=")
print(b)

V=a*x+b
print("V=")
print(V)
temp=V/1023
print("temp=")
print(temp)