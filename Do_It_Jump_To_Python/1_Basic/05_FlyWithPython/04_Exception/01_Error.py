# coding: utf-8

# 어떤 상황에서 오류가 발생하는지 알아보자.
# 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류.
# f = open('없는파일', 'r')
'''
Traceback (most recent call last):
  File "/01_Error.py", line 5, in <module>
    f = open('없는파일', 'r')
IOError: [Errno 2] No such file or directory: "\xec\x97\x86\xeb\x8a\x94\xed\x8c\x8c\xec\x9d\xbc"
'''
# 0으로 나누기를 시도 했을 경우.
# 4 / 0
'''
Traceback (most recent call last):
  File "01_Error.py", line 12, in <module>
    4 / 0
ZeroDivisionError: integer division or modulo by zero
'''
# 없는 인덱스 값을 찾으려 했을 경우
# a = [1, 2, 3]
# a[4]
'''
Traceback (most recent call last):
  File "/01_Error.py", line 20, in <module>
    a[4]
IndexError: list index out of range
'''