# coding: utf-8
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

'''ZeroDivisionError: integer division or modulo by zero'''
# a = FourCal(4, 0)
# print( a.div() )



# Override : 상속한 클래스에 있는 메소드를 재정의
class SafeFourCal( FourCal ):
  def div(self):
    if self.second == 0:
      return 0
    else:
      return self.first / self.second

a = SafeFourCal(4, 0)
print( a.div() )