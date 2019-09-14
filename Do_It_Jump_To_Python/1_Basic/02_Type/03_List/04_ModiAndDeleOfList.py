# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)
'''
리스트 수정과 삭제
'''
title(' 리스트에서 값 수정하기 ')
a = [1, 2, 3]
a[1] = 4
print(a)

'''
del() 함수는 파이썬 내장 삭제함수로 `del 객체 ` 로 사용한다.
'''
title(' 리스트 요소 삭제하기 del()')
del a[1]
print(a)

title(' 슬라이싱 기법을 사용한 리스트 요소 삭제하기. ')
a = [1, 2, 3, 4, 5]
del a[3:]
print( a )

'''
remove와 pop 함수도 있다.
'''
