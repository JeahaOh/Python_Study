# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 조건문이란? ' )

money = 2000
if money >= 3000:
  print(' 택시 타고 간다. ')
else:
  print(' 걸어서 간다. ')

title( ' and, or, not ' )
card = True
if money >= 3000 or card:
  print(' 택시 타고 간다. ')
else:
  print(' 걸어서 간다. ')

title( ' x in s, x not in s ')
print( 1 in [1, 2, 3])
print( 1 not in [1, 2, 3])
print( 'a' in ('a', 'b', 'c') )
print( 'j' not in 'python' )

pocket = ['paper', 'cellphont', 'money']
if 'money' in pocket:
  print(' Taxi ')
else:
  print(' Walk ')

title( ' pass ' )
if 'money' in pocket:
  pass
else:
  print('CARD')