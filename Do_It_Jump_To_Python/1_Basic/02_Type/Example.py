# coding: utf- 8

print( ( 80 + 75 + 55 ) / 3 )

print( 13 % 2 )

pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print( yyyymmdd )
print( num )

print( pin[7] )

a = 'a:b:c:d'
b = a.replace(':', '#')
print( b )

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print( a )

a = ['Life', 'is', 'too', 'short']
result = " ".join( a )
print( result )

a = (1, 2, 3)
a = a + (4,)
print( a )

a = (1, 2, 3)
print( id( a ) )

a = a + (4,)
print( a )
print( id( a ) )

# a[[1]] = 'python'

a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B')
print( a )
print( result )

a = [ 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

aSet = set( a )
b = list(aSet)
print( b )
