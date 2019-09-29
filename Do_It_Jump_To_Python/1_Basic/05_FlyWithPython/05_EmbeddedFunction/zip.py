# coding: utf-8
'''
zip( *iterable )
동일한 개수로 이루어진 자료형을 묶어준다

?
'''
print( list(zip([1, 2, 3], [4, 5, 6])) )
print( list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))  )
print( list(zip("abc", "def")) )

