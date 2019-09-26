# coding: utf-8
# 모듈 만들기
# *.py로 만들어진 모든 python 파일은 모듈이다.
def add( a, b ):
  return a + b
def sub( a, b ):
  return a - b

'''
모듈 불러오기
terminal에서 해당 파일이 있는 곳으로 이동.
python Interpreter 실행

"""
>>> import mod1 (.py를 제외한 파일의 이름))
>>> print( mod1.add( 3, 4 ) )
7
>>> print( mod1.sub( 4, 2 ) )
2
"""
import : 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어.
모듈의 함수를 사용하기 위해 . 도트 연산자를 사용.

모듈 이름 없이 함수 이름만 쓰고싶을 경우.
"""
>>> from  mod1 import add
>>> add( 3, 4 )
"""

"""
>>> from mod1 import add, sub
>>> from mod1 import *
"""

'''