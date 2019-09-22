# coding: utf-8
'''
객체 변수는 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지한다는 점은 앞에서 알아보았다.
이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아보자.
클래스 안에 변수를 선언해서 생성한다.
'''
class Clazz:
  var = 'ASDF'

print( Clazz.var )

a = Clazz()
print( a.var )

b = Clazz()
print( b.var )

Clazz.var = "QWERTY"
print( a.var )
print( b.var )

print( id( Clazz.var ) )
print( id( a.var ) )
print( id( b.var ) )

# 클래스 변수는 클래스로 만든 모든 인스턴스에서 공유된다.