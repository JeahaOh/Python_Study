# coding: utf-8
import time
head = time.strftime('%x', time.localtime(time.time()))
tail = time.strftime('%X', time.localtime(time.time()))
print( head + ' ' + tail )

t = time.strftime( '%Y/%m/%d %H:%M:%S' )
print( t )