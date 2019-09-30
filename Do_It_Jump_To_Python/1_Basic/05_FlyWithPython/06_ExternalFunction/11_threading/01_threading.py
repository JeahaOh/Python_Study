# coding: utf-8
import time

# 5초의 시간이 걸리는 함수.
def long_task():
  for i in range( 5 ):
    # 1초간 대기한다.
    time.sleep(1)
    print( 'working : %s\n' % i )

print( 'START' )

# long_task()를 5번 실행한다.
for i in range( 5 ):
  long_task()

print( 'END' )