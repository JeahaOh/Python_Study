# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 함수 안에서 선언한 변수의 효력 범위 ' )

a = 1
def vartest( a ):
  a += 1

vartest( a )
print( a )

title( ' 함수 안에서 함수 밖의 변수 변경하기 ' )

title( ' 1. return ')
v1 = 1
def return_var( v1 ):
  v1 += 1
  return v1

v1 = return_var( v1 )
print( v1 )

title( ' 2. global ')
v2 = 1
def global_var():
  # global v2는 함수 밖의 v2 변수를 직접 사용하겠다는 선언
  global v2
  v2 += 1

global_var()
print( v2 )
