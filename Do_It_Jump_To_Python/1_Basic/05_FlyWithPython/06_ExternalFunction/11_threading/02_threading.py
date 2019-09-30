# coding: utf-8
import time
# 스레드를 생성하기 위해서 threading 모듈이 필요하다.
import threading

def long_task():
  for i in range( 5 ):
    time.sleep(1)
    print( 'working : %s\n' % i )

print( 'START' )

threads = []

for i in range( 5 ):
  # 스레드를 생성한다.
  t = threading.Thread( target= long_task )
  threads.append( t )

for t in threads:
  # 스레드를 실행한다.
  t.start()

print( 'END' )