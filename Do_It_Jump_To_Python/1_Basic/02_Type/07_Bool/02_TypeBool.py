# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

'''
자료형에도 참과 거짓이 있다.
문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓이 된다.
비어있지 않으면 참이 된다.
숫자는 값이 0일 경우 거짓이 된다.
None은 다음에 배우도록 하자.
'''
def TF( val ):
  if val:
    print( val , True )
  else:
    print( val , False)

title( ' 자료형의 참 거짓 ' )
TF( 'python' )
TF( "" )
TF( [1, 2, 3] )
TF( [] )
TF( () )
TF( {} )
TF( 1 )
TF( 0 )
TF( None )

title( ' 참과 거짓의 사용 ' )
a = [1, 2, 3, 4]
while a:
  print( a.pop() )