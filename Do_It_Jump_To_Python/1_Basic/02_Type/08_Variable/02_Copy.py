# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)


title( ' 리스트를 복사하고자 할 때 ' )
a = [1, 2, 3]
b = a
print( b )

'''
b는 a와 완전히 동일하다고 할 수 있다.
다만 [1, 2, 3] 리스트를 참조하는 변수가 a 변수 1개에서 b 변수가 추가되어 2개로 늘어났다는 차이만 있을 뿐이다.
'''
print( id(a) )
print( id(b) )

# 두개의 값이 동일하다. a와 b가 가리키는 대상이 동일하다는 뜻

print( a is b )

# 동일한 객체를 가리키고 있는지에 대해 판단하는 is 함수로도 True가 반환된다.

a[1] = 4
print( a )
print( b )

# a 리스트의 두번째 요소를 바꾸니 b에서도 바뀜.
# c 변수를 생성할 때, a 변수의 값을 다 가져오면서 다른 주소를 가리키도록 하는 방법을 알아보자.

title( '1. [:] 이용 ')
# 리스트 전체를 가리키는 [:]를 이용해서 복사
a = [1, 2, 3]
c = a[:]
a[1] = 4
print( a )
print( c )

title( '2. copy 모듈 이용 ')
from copy import copy
d = copy( c )

print( c is d )   # False

title( '변수를 만드는 여러가지 방법 ')
a, b = ('Python', 'Life')
print( a )
print( b )
(a, b) = 'Python', 'Life'
print( a )
print( b )
[a, b] = ['Python', 'Life']
print( a )
print( b )
a = b = 'Py'
print( a )
print( b )

title( ' 두 변수의 값 바꾸기 ')
a = 3
b = 5
a, b = b, a
print( a )
print( b )