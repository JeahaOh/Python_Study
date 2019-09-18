# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 일반적인 함수 ' )
'''
def 함수명( 매개변수 ):
  <수행할 문장>
  return 결과값
'''
def add( a, b):
  result = a + b
  return result
'''
함수 이름은 add이고,
a와 b를 받아 두 값을 더한 값을 반환한다.
'''

a = 3
b = 4
c = add( a, b )
print( c )

'''
입력값과 결과값이 있는 함수는 다음과 같이 사용한다.
결과값을 받을 변수 = 함수이름( 인자1, 인자2, ... )

매개변수와 인자
매개변수(parameter)와 인자(arguments)는 혼용되서 사용된다.
매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고,
인자는 함수를 호출할 때 전달하는 입력값을 의미한다.
'''

title( ' 입력값이 없는 함수 ')
def returnSentence():
  return 'HI'

a = returnSentence()
print( a )
'''
입력값이 없고 결과값만 있는 함수는 다음과 같이 사용한다.
결과값을 받을 변수 = 함수이름()
'''

title( ' 결과값이 없는 함수 ' )
def printAddResult( a, b):
  print('%d, %d의 합은 %d.' % (a, b, a + b))

printAddResult( 3, 4 )
#a = printAddResult( 3, 4 )
#print( a )  # None은 False를 나타내는 자료형. 

'''
결과값이 없는 함수는 다음과 같이 사용한다.
함수이름( 인자1, 인자2 )
'''

title( ' 입력값도 결과값도 없는 함수 ' )
def say():
  print( 'HI' )

say()