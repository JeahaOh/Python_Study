# coding: utf-8
'''
# 예외 발생 시키기
Python은 raise 명령어를 사용해 오류를 강제로 발생기킬 수 있다.

Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 강제로 구현하도록 만들 수 있다.
'''
class Bird:
  def fly( self ):
    raise NotImplementedError
    # NotImplementedError는 파이썬 내장 오류로,
    # 꼭 작성해야 하는 부분이 구현되지 않았을 경우 예외를 발생시킨다.

'''
class Eagle( Bird ):
  pass

eagle = Eagle()
eagle.fly()
"""
NotImplementedError
"""
'''
class Eagle( Bird ):
  def fly( self ):
    print( 'Fly Fast')

eagle = Eagle()
eagle.fly()