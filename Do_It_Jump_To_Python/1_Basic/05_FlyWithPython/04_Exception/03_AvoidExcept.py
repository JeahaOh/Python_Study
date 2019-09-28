# coding: utf-8
'''
# 오류 회피하기
특정 오류가 발생할 경우 그냥 통과시켜야 할 경우가 있다.
try 문 안에서 FileNotFoundError가 발생할 경우 pass를 사용하여 오류를 회피하도록 작성한 예이다.
'''
print( 'start' )
try:
  f = open( 'NULL', 'w' )
except FileNotFoundError:
  pass
print( 'end' )