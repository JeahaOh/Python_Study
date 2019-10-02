# coding: utf-8
import sys

'''
def argvSum( params ):
  sum = 0
  for i in params:
    try:
      sum += int( i )
    except: pass
  
  print( sum )

argvSum( sys.argv )
'''

numbers = sys.argv[1:]

result = 0
for number in numbers:
  result += int( number )

print( result )