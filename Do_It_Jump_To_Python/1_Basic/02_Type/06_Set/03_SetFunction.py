# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

s1 = set([1, 2, 3])

title( ' 1개의 값 추가하기 add ' )
# 이미 만들어진 set에 1개의 값을 추가할 경우에는 다음과 같이 한다.
s1.add( 4 )
print( s1 )

title( ' 여러개의 값 추가하기 update ')
# 여러개의 값을 한꺼번에 추가할 때는 update()를 사용한다.
s1.update([4, 5, 6])
print( s1 )

title( ' 특정 값 제거하기 ' )
# 특정 값을 제거하고 싶을 때는 다음과 같이 한다.
s1.remove( 2 )
print( s1 )