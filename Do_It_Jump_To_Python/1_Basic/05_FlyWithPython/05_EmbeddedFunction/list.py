# coding: utf-8
'''
list( x )
반복 가능한 자료형 x를 list로 반환
'''
print( list('Python') )
print( list( [1, 2, 3] ) )
print( list( ("a", 2) ) )

a = [1, 2, 3]
b = list( a )

print( id(a) )
print( id(b) )