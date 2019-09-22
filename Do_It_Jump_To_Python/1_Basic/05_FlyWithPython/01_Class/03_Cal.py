# coding: utf- 8

class Calculator:
  def __init__( self ):
    self.result = 0

  def add( self, n ):
    self.result += n
    return self.result
  
  def sub( self, n ):
    self.result -= n
    return self.result

cal1 = Calculator()
cal2 = Calculator()

print( cal1.add(3) )
print( cal1.add(4) )

print( cal2.add(3) )
print( cal2.add(7) )