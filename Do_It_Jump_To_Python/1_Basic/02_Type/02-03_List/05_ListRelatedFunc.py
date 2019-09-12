# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)
'''
리스트 관련 함수
'''
title(' 리스트에 요소 추가 append ')
a = [1, 2, 3]
a.append(4)
print( a )

a.append( [5, 6] ) 
print( a )

title(' 리스트 정렬 sort ')
a = [1, 4, 2, 3]
b = ['b', 'd', 'c', 'a', 'f', 'g', 'e']
b.sort()
a.sort()
print( a )
print( b )

title(' 리스트 뒤집기 ')
a.reverse()
print( a )

title(' 위치 반환 index ')
print( a.index(2) )
# print( a.index(9) )
'''
리스트에 없는 값을 찾으면 ValueError가 발생한다.
Traceback (most recent call last):
  File "/Users/Jeaha/git/Python_Study/Py/Python_Study/02_Type/02-03_List/05_ListRelatedFunc.py", line 29, in <module>
    print( a.index(9) )
ValueError: 9 is not in list
'''

title(' 리스트에 요소 삽입 insert ')
# 0번 index에 9를 넣어보자..
a.insert( 0, 9 )
a.insert( 5, 3)
print( a )

title(' 리스트에서 요소 제거  remove')
# a가 3이라는 값을 2개 가지고 있을 경우 첫 번빼 3만 제거됨.
a.remove(3)
print( a )



title(' 리스트에 요소 꺼내기 pop')
# 리스트의 맨 마지막 요소를 반환하고, 그 요소는 삭제함.
print( a.pop() )
print( a )

# pop( x )는 x 번째 요소를 반환하고, 그 요소는 삭제한다.
print( a.pop(1) )
print( a )

a.insert(2, 4)
a.insert(len(a), 4)
title(' 리스트에 포함된 요소 x의 개수 세기 count ')
print( a )
print( a.count(4) )

title(' 리스트 확장 extend ')
# extend()는 +=와 같다.
a.extend([8, 6])
print( a )
a.extend( b)
print( a )