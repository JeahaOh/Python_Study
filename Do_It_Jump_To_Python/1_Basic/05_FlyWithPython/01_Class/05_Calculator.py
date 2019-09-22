# coding: utf- 8
class FourCal:
  # 메소드의 첫 번째 매개변수 self를 명시적으로 구현하는 것을 python만의 독특한 특징이다.
  def setData(self, first, second):
    self.first = first
    self.second = second

a = FourCal()
a.setData( 4, 2 )

b = FourCal()
FourCal.setData( b, 3, 5 )

print( type( a ) )
print( type( b ) )

print( a.first )
print( a.second )

print( b.first )

print( id(a.second) )
print( id(b.second) )