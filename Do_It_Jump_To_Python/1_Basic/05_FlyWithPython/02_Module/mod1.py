# coding: utf-8
# *.py로 만들어진 모든 python 파일은 모듈이다.
def add( a, b ):
  return a + b
def sub( a, b ):
  return a - b

if __name__ == "__main__":
  print( add( 1, 4 ) )
  print( sub( 4, 2 ) )