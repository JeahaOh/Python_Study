# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

title( ' 교집합 ' )
# & 기호 하나면 교집합을 간단히 구할 수 있다.
print( s1 & s2 )

# intersection())를 사용할 수도 있다.
print( s1.intersection( s2 ) )

title( ' 합집합 ' )
# | 기호나 union()를 사용할 수 있다.
print( s1 | s2 )
print( s1.union( s2 ) )

title( ' 차집합 ' )
# - 기호나 difference()를 사용할 수 있다.
print( s1 - s2 )
print( s2 - s1 )

print( s1.difference( s2 ) )
print( s2.difference( s1 ) )