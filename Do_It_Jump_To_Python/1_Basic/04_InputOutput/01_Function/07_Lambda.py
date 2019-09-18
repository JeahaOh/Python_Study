# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' Lambda ' )
'''
Lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
보통 함수를 간결하게 만들 때 사용한다.
def를 사용할 정도로 복잡하지 않거나, def를 사용할 수 없는 곳에 주로 사용한다.

lamda 매개변수1, 매개변수 2, ... : 매개변수를 이용한 표현식
'''
add = lambda a, b: a + b
result = add( 3, 4 )
print( result )

print( lambda : 1 + 2 )