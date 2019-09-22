# coding: utf- 8
class FourCal:
  # __init__()는 a = FourCal()를 호출할 때 실행된다.
  def __init__(self, first, second):
    self.first = first
    self.second = second
  # 따라서 setData는 따로 필요하지 않다.
  '''
  def setData(self, first, second):
    self.first = first
    self.second = second
  '''
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    return self.first * self.second
  def sub(self):
    return self.first - self.second
  def div(self):
    return self.first / self.second

a = FourCal(4, 2)

print( a.add() )
print( a.mul() )
print( a.sub() )
print( a.div() )

b = FourCal(3, 8)
print( b.add() )
print( b.mul() )
print( b.sub() )
print( b.div() )