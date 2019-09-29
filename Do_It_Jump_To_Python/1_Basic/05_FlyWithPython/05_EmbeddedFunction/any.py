# coding: utf-8
'''
any( x )
반복 가능한(literable) 자료형을 인자로 받음.
  - List,m Tuple, String, Dictionary, Set
x중 하나라도 참이면 True, 하나라도 거짓이면 False를 반환
'''
print( any( [True, True] ) )    # T
print( any( [True, False] ) )   # T
print( any( [False, False] ) )  # F
print( any( [0, 1, 2, 3] ) )    # T
print( any( [0, ""] ) )         # F