# coding: utf- 8
class FourCal:
  def setData(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    return self.first * self.second
  def sub(self):
    return self.first - self.second
  def div(self):
    return self.first / self.second

a = FourCal()
a.setData( 4, 2 )

print( a.add() )
print( a.mul() )
print( a.sub() )
print( a.div() )

b = FourCal()
b.setData( 3, 8 )

print( b.add() )
print( b.mul() )
print( b.sub() )
print( b.div() )