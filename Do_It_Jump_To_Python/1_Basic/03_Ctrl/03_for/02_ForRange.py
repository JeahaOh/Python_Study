# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' range( 10 ) ')
# for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다.
a = range( 10 )
print( a )
# range( 10 )은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 준다.

title( ' range( 1, 11 )')
# 시작 숫자와 끝 숫자를 지정하면 range( 시작 숫자, 끝 숫자 ) 형태를 사용하는데 끝 숫자는 포함되지 않는다.
a = range( 1, 11 )
print( a )

title( ' range()의 예시 ')
# for와 range()를 사용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현할 수 있다.
add = 0
for i in range( 1, 11 ):
  add += i

print( add )

marks = [90, 25, 67, 45, 80]
for num in range( len( marks ) ):
  if marks[num] < 60:
    continue
  print( '%d번 합격.' % (num + 1 ) )

title( ' for range를 이용한 구구단 ' )
# for와 range()를 사용하면 코드 4줄로 구구단을 출력할 수 있다.
for i in range( 2, 3 ): # 2, 10
  for j in range( 1, 10 ):
    # print( i * j, end="" )
    print( i * j )
  print( ' ' )


title( ' List Comprehension 사용하기 ' )
# 리스트 안에 for문을 포함하는 리스트 내포를 사용하면 좀더 편리하고 직관적인 프로그래밍을 할 수 있다.
a = [1, 2, 3, 4]
result = []
for n in a:
  result.append( n * 3 )

print( result ) # [3, 6, 9, 12]

# List Comprehension
a = [1, 2, 3, 4]
result = [ n * 3 for n in a ]
print( result ) #[3, 6, 9, 12]

# 짝수에만 3을 곱한다면
a = [1, 2, 3, 4]
result = [ n * 3 for n in a if n % 2 == 0]
print( result ) # [6, 12]

'''
리스트 내포의 일반 문법은 다음과 같다
[ 표현식 for 항목 in 반복가능객체 if 조건문 ]

for문을 2개 이상 사용하는 것도 가능하다
[ 표현식 for 항목1 in 반복가능객체1 if 조건문1
  for 항목2 in 반복가능객체2 if 조건문2
  ...
  for 항목n in 반복가능객체n if 조건문n ]
'''
print(
  [ x * y for x in range( 2, 10 )
          for y in range( 1, 10 ) ]
)