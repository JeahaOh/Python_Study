# coding: utf- 8

result = 0

def add(n):
  global result
  result += n
  return result

print( add(3) )
print( add(4) )