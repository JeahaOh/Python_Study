# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

## 튜플의 요솟값을 삭제하려고 시도하면.
'''
t1 = (1, 2, 'a', 'b')
del t1[1]
TypeError: 'tuple' object doesn't support item deletion
요소를 지우는 행위가 지원되지 않음.
'''

## 튜플의 요솟값을 변경하려고 시도하면.
'''
t1 = (1, 2, 'a', 'b')
t1[0] = 'c'
TypeError: 'tuple' object does not support item assignment
요소를 변경하는 행위가 지원되지 않음.
'''
title(' 인덱싱 하기 ')
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

title(' 슬라이싱 하기 ')
print(t1[1:])   # <- t1[1]부터 끝까지


title(' 튜플 더하기 ')
t2 = 3, 4
print( t1 + t2 )

title(' 튜플 곱하기 (반복하기) ')
print( t2 * 4 )

title(' 튜플 길이 구하기 ')
print( len(t1) )

title(' 튜플 값 추가하기 ')
print( t1 + (4,))