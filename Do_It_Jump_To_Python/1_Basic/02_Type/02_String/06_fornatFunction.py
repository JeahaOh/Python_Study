
## format 함수를 사용한 포매팅
# 숫자 바로 대입하기
print('I eat {0} apples'.format(3))

# 문자열 바로 대입하기
print('I eat {0} apples'.format('five'))

# 숫자 값을 가진 변수로 대입하기
n = 7
print('I eat {0} apples'.format(n))

# 2개 이상의 값 넣기
## {}의 숫자는 format 인자의 index.
n = 1
day = 'one'
print('I ate {0} apples. so I was sick for {1} days.'.format(n, day))

# 이름으로 넣기
print('I ate {number} apples. so I was sick for {day} days.'.format(number = 2, day = 'two'))

# 인덱스와 이름 혼용해서 넗기
print('I ate {0} apples. so I was sick for {day} days.'.format(3, day = 'three'))

# 왼쪽 정렬
print('> {0:<10} <'.format('fuck'))

# 가운데 정렬
print('> {0:^10} <'.format('fuck'))

# 오른쪽 정렬
print('> {0:>10} <'.format('fuck'))

# 공백 채우기
print('> {0:=^10} <'.format('fuck'))
print('> {0:!<10} <'.format('fuck'))

# 소수점 표현하기
y = 3.43214
print('{0:0.2f}'.format(y))
print('{0:0.4f}'.format(y))
print('{0:10.4f}'.format(y))
print('{0:0>10.4f}'.format(y))

# {} 표현하기
print('{{ and }}'.format())

'''
# f문자열 포매팅
문자열 앞에 접두사 f를 쓰면 f문자열 포매팅 가능.
변수를 생성한 후 그 값을 참조시키는 것.
파이썬 3.6 미만 버전에서는 사용 불가.
'''
name = 'ASDF'
age = 28
print(f'name : {name}, age : {age - 1}')

'''
딕셔너리는 02-05에서 알아본다.
딕셔너리는 f문자열 포매팅에서 다음과 같이 사용할 수 있다.
'''
d = {'name' : 'ASDF', 'age' : 28}
print(f'name => {d["name"]}\nage => {d["age"]}')

