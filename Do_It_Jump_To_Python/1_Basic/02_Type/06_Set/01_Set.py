# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title(' 집합 자료형 만들기 set ')
# set()안에 리스트를 입력하여 만들 수 있다.
s1 = set([1, 2, 3])
print( s1 )

# 문자열을 입력하여 만들 수 있다.
s2 = set('Hell The Python')
print( s2 )

# 빈 집합은 set()으로 만들 수 있다.
s3 = set()
print( s3 )
'''
set의 특징.
- 중복 허용 X
- 순서 X

리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만,
set 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
만약, set에 저장된 값을 인덱싱 하고 싶다면 다음과 같이 리스트나 튜플로 변환한 후 접근해야 한다.
# 중복을 허용하지 않기 때문에 set은 자료헝의 중복을 제거하기 위한 필터로 사용하기도 함.
'''
title(' set에 인덱싱 하기 ')
s1 = set([4, 2, 1, 3])
print( s1 )

l1 = list( s1 )
print( l1 )
print( l1[0] )

t1 = tuple( s1 )
print( t1 )
print( t1[0] )