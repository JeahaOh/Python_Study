
'''
# f문자열 포매팅
문자열 앞에 접두사 f를 쓰면 f문자열 포매팅 가능.
변수를 생성한 후 그 값을 참조시키는 것.
파이썬 3.6 미만 버전에서는 사용 불가.
'''
name = 'ASDF'
age = 28
print(f'name => {name}\nage => {age - 1}')

'''
딕셔너리는 02-05에서 알아본다.
딕셔너리는 f문자열 포매팅에서 다음과 같이 사용할 수 있다.
'''
d = {'name' : 'ASDF', 'age' : 28}
print(f'name => {d["name"]}\nage => {d["age"]}')

# fString 정렬
print(f'> {"asdf":<10} <')
print(f'> {"asdf":>10} <')
print(f'> {"asdf":^10} <')

# fString 공백 채우기
print(f'> {"F"::^10} <')
print(f'> {"F":!<10} <')

# 소숫점 표현
y = 3.42134234
print(f'{y:0.2f}')
print(f'{y:0.4f}')
print(f'{y:10.2f}')

# {}
print(f'{{ and }}')

print(f'{"Python":!^12}')
print('{0:!^12}'.format('Python'))