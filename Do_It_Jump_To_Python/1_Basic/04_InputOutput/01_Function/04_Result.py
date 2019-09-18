# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 함수의 결과값은 언제나 하나이다. ' )

def add_and_mul( a, b ):
  return a + b, a * b

result = add_and_mul( 3, 4 )
print( result )
'''
result는  a + b와 a * b 2개인데
add_and_mul의 리턴값은 튜플값 하나인 (a + b, a * b)을 리턴한다.
만약 튜플의 값을 2개의 결과값으로 받고 싶다면 다은과 같이 함수를 호출하면 된다.
'''
result1, result2 = add_and_mul( 3, 4 )
print( result1 )
print( result2 )

