# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 입력값이 몇 개가 될지 모를 때 ' )
'''
입력값이 여러 개일 때,
몇 개가 입력될지 모를 때 다음과 같은 방법을 쓴다.

def 함수이름( *매개변수 ):
  <수행할 문장>
  ...

*을 붙이면 입력값을 전부 모아 튜플로 모아준다.
'''
title( ' 여러개의 입력값을 받는 함수 만들기 ' )
def add_many( *args ):
  print( args )
  result = 0
  for i in args:
    result += i
  
  return result

print( add_many( 1, 2, 3 ) )
print( add_many( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) )

title( '  ' )

def add_or_mul( choice, *args):
  print( choice )
  if choice == 'add':
    result = 0
    for i in args:
      result += i
  elif choice == 'mul':
    result = 1
    for i in args:
      result *= i
  
  return result

print( add_or_mul('add', 1, 2, 3, 4, 5) )
print( add_or_mul('mul', 1, 2, 3, 4, 5) )

title( ' 키워드 파라미터 kwargs ')
'''
키워드 파라미터를 사용할 때는 매개변수 앞에 **를 붙인다.
매개변수 이름 앞에 **를 붙이면 매개변수는 딕셔너리가 되고,
모든 key=value 형태의 입력값이 그 딕셔너리에 저장된다.

kwargs는 keyword arguments의 약자.
'''
def print_kwargs( **kwargs ):
  print( kwargs )

print_kwargs( a = 1 )
print_kwargs( name='foo', age='2' )