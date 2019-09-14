# coding: utf- 8
'''
문자열 관련 함수
문자열 자료형은 내장함수를 가지고 있음.  
'''

# 문자열에서 특정 문자의 개수 세기
a = 'hobby'
print(a.count('b'))

print('-' * 20)
# 문자열에서 특정 문자의 index 찾기
a = 'Python is the best choice'
print(a.find('b'))
print(a.find('k'))

print(a.index('b'))
#print(a.index('k'))
## index()는 없는 문자를 찾으면 에러가 남.

print('-' * 20)
# 문자열 삽입 ASDF 각 문자 사이에 ,를 삽입.
print(','.join('ASDF'))
print(','.join(['a', 's', 'd', 'f']))

print('-' * 20)
# upper & lower
print('fuck'.upper())
print('FUCK'.lower())

print('-' * 20)
# 공백 지우기 strip() lstrip() rstrip()
a = '  4246  '
print('>' + a + '<')
print('>' + a.rstrip() + '<')
print('>' + a.lstrip() + '<')
print('>' + a.strip() + '<')

# 문자열 바꾸기 replace
a = 'Life is Too Short'
print(a.replace('Life', 'Your thought'))

print('-' * 20)
# 문자열 나누기 split
print(a.split())
b = 'a, b, c, d, e'
print(b.split(', '))