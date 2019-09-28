# coding: utf-8
'''
특수한 경우에만 예외를 처리하기 위해 Exception 클래스를 상속해서 예외를 만들어 사용한다.
직접 예외를 만들어 보자.
'''
# class MyError( Exception ):
#   pass

class MyError( Exception ):
  '''
    오류 메세지를 출력했을 때 오류메세지를 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메소드를 구현해야 한다.
  '''
  def __str__( self ):
    return '\n\tUNACCEPTABLE NICK\n'

def say_nick( nick ):
  if nick == 'dumb ass':
    raise MyError()
  print( nick + "\n" )

say_nick( 'Holy Fucker' )
# say_nick( 'dumb ass' )

'''
Holy Fucker

Traceback (most recent call last):
  File "/05_MakeExcept.py", line 15, in <module>
    say_nick( 'dumb ass' )
  File "/05_MakeExcept.py", line 11, in say_nick
    raise MyError()
__main__.MyError
'''

try:
  say_nick( 'dumb ass' )
except MyError as e:
  print( 'Prevented Nick' )
  print( e )