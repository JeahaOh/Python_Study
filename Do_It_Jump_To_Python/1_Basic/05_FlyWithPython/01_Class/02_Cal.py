# coding: utf- 8

result1 = 0
result2 = 0

def add1( n ):
  global result1
  result1 += n
  return result1

def add2( n ):
  global result2
  result2 += n
  return result2

print( add1(3) )
print( add1(4) )

print( add2(3) )
print( add2(7) )