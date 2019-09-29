# coding: utf-8
'''
filter
첫 번째 인수로 함수 이름을,
두 번째 인수로 그 함수에 들어갈 반복 가능한 자료형을 받는다.
그리고 두 번째 인수가 첫 번째 인수인 함수에 입력 되었을 때 반환 값이 참인 것만 묶어서 반환.
'''
def positive( l ):
  result = []
  for i in l:
    if i > 0:
      result.append( i )

  return result

print( positive( [1, -3, 2, 0, -5, 6] ) )

# 위의 함수를 아래와 같이 간단하게 할 수 있다.
def posi( x ):
  return x > 0

print( filter( posi, [1, -3, 2, 0, -5, 6] ) )

# lambda를 이용하면 더 간단하게 할 수 있다.
print( filter( lambda x: x > 0, [1, -3, 2, 0, -5, 6] ) )
print( filter( lambda x: x > 0, [1, -3, 2, 0, -5, 6] ) )