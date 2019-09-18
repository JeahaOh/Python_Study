# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 매개변수 지정하여 호출하기 ' )

def func( a, b ):
  print( 'a : %d\nb : %d\n' % (a, b) )

'''
함수를 호출할 때 매개변수를 지정할 수도 있다.
다음과 같이 매개변수를 지정하여 사용할 수 있다.
매개변수를 지정하면 순서에 상관없이 사용할 수 있다는 장점이 있다.
'''
func( a=1, b=2 )
func( b=4, a=3)