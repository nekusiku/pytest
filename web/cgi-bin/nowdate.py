#!/usr/bin/env python
# -*- coding:utf-8-*-
import datetime
import time
#import threading
#import Tkinter

html_body="""
<html><body>
%d/%d/%d %d:%d:%d
</body></html>"""

now=datetime.datetime.now()
#seconds = datetime.timedelta(seconds)
#while (seconds = seconds+1){
def clock():
    print "Content-type: text/html\n"
    print html_body % (now.year, now.month, now.day, now.hour, now.minute, now.second)


#timer = Threading.Timer(1,clock)
#timer.mainloop
#}
