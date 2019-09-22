# coding: utf- 8
class FourCal:
  def __init__(self, first, second):
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

# 상속의 개념은 Java와 같다.
# Python의 상속은
# class 클래스 이름( 상속할 클래스 이름)
# 로 선언한다
class MoreFourCal( FourCal ):
  def pow(self):
    return self.first ** self.second

a = MoreFourCal(4, 2)
print( a.add() )
print( a.mul() )
print( a.pow() )