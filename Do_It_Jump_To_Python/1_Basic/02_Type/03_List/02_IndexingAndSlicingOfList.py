# coding: utf- 8
'''
리스트의 인덱싱과 슬라이싱
리스트도 문자열처럼 인덱싱과 슬라이싱이 가능함.
'''

# 리스트의 인덱싱
print('-' * 10 + '리스트의 인덱싱' + '-' * 10)
a = [1, 2, 3]
print(a)
print( a[0] )
print( a[0] + a[2] )

# 음수 index는 뒤에서부터 센다.
print( a[-1] )

# 리스트 안의 리스트
print('-' * 10 + '리스트안의 리스트' + '-' * 10)
a = [1, 4, 8, ['Fuck', 'Python']]
print( a[0] )
print( a[-1] )
print( a[3] )

# 리스트 안의 리스트에서 값 꺼내기
print('-' * 10 + '2중 리스트에서 값 꺼내기' + '-' * 10)
print( a[-1][1])

## 3중 리스트에서 인덱싱 하기
print('-' * 10 + '3중 리스트에서 값 꺼내기' + '-' * 10)
a = [1, 2, ['a', 'b', ['Fill', 'My', 4246]]]
print(a[2][2][2])

# 리스트의 슬라이싱
## 문자열에서 슬라이싱하는 방법과 완전히 같다.
print('-' * 10 + ' 리스트의 슬라이싱 ' + '-' * 10)
a = [1, 2, 3, 4, 5]
print( a[0:3] )
b = a[:2]
c = a[2:]
d = a[1:3]
print( b )
print( c )
print( d )