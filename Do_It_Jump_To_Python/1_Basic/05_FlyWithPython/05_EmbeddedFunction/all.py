# coding: utf-8
'''
all( x )
반복 가능한(literable) 자료형을 인자로 받음.
  - List,m Tuple, String, Dictionary, Set
x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 반환함.
'''
print( all( [True, True] ) )  # T
print( all( [1, 2, 3] ) )     # T
print( all( [0, 1, 2, 3] ) )  # F