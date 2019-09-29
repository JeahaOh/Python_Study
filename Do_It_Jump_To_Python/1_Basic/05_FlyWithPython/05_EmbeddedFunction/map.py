# coding: utf-8
'''
map( f, iterable )
함수 f와 반복 가능한 iterable 자료형을 받는다.
입력 받은 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려주는 함수이다.
'''
def two_times( numList ):
  result = []
  for num in numList:
    result.append( num * 2 )
  return result

result = two_times( [1, 2, 3, 4] )
print( result )

def two_timez( x ):
  return x * 2

result = map( two_timez, [1, 2, 3, 4] )
print( result )

print( map( lambda x: x * 2, [1, 2, 3, 4] ) )
