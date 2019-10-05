# coding: utf-8
def GuGu( n ):
  result = []
  i = 1
  while i < 10:
    result.append( n * i )
    i += 1

  return result

j = 2
while j < 10:
  print( GuGu( j ) )
  j += 1
