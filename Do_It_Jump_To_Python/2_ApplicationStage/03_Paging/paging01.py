# coding: utf-8
def getTotalPage( m, n ):
  return m // n + 1

print( getTotalPage( 5, 10 ) )    # 1
print( getTotalPage( 15, 10 ) )   # 2
print( getTotalPage( 25, 10 ) )   # 3
print( getTotalPage( 30, 10 ) )   # 4