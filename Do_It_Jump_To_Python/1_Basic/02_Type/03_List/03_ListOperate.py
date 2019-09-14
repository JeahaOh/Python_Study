# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)
'''
리스트 연산
리스트 역시 +, * 연산 기호를 사용해서 연산할 수 있다.
'''

title(' 리스트 더하기 + ')
a = [1, 2, 3]
b = [4, 5, 6]
print( a + b )

title(' 리스트 반복하기 * ')
a = ['Fuck', 'My', 'Life']
print( a * 4 )

title(' 리스트 길이 구하기 len() ')
print( len(a) )

title(' 자주 하는 연산 오류 ')
# print( a[0] + b[2] )
'''
Traceback (most recent call last):
  File "/Users/Jeaha/git/Python_Study/Py/Python_Study/02_Type/02-03_List/03_ListOperate.py", line 22, in <module>
    print( b[2] + 'hi' )

TypeError: unsupported operand type(s) for +: 'int' and 'str'

The terminal process terminated with exit code: 1

정수와 문자열을 더하려 해서 TypeError 가 남.
숫자와 문자열을 더하고 싶다면 숫자를 문자로 바꿔줘야 함.
'''
title(' 숫자를 문자로 바꿔주는 str() ')
print( a[0] + str(b[2]) )