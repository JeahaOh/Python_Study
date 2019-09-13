# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)
  

title(' 딕셔너리 쌍 추가하기 ')
a = {1: 'a'}
a[2] = 'b'
a['Idiot'] = 'Jeaha'
a[3] = [177, 74,28]
print(a)

title(' 딕셔너리 요소 삭제하기 ')
del a[1]
print( a )

title(' Key를 사용해 Value 얻기 dictionary[KEY] ')
print( a['Idiot'])
print( a[3])    # <- 인덱스를 의미하는것이 아닌 Key를 의미함.

title(' 중복된 key ')
b = {1 : 'a', 1 : 'B'}
print(b[1])

title(' key로써 tuple ')
c = {(1, 2): 'tuple key의 value'}
print(c[(1,2)])