# coding: utf- 8
def increment( a ):
  a += 1

num = 1
increment( num )
print( num )  # 1

def add_more( l ):
  print( id(l) )
  l.append( 5 )

my_list = [1, 2, 3, 4]
add_more( my_list )

print( my_list )
print( id(my_list) )


def clean_it(l):
  print( id(l) )
  l = []
  print( id(l) )

clean_it(my_list)

print( my_list )

# https://code13.tistory.com/214