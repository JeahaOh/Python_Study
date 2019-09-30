# coding: utf-8
import time
import threading

def long_task():
  for i in range( 5 ):
    time.sleep(1)
    print( 'working : %s\n' % i )

print( 'START' )

threads = []

for i in range( 5 ):
  t = threading.Thread( target= long_task )
  threads.append( t )

for t in threads:
  t.start()

for t in threads:
  # join()으로 스레드가 종료될 때까지 기다린다.
  t.join()

print( 'END' )