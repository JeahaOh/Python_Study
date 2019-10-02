# coding: utf-8
import random

pair = []
while len(pair) < 6:
  n = random.randint( 1, 45 )
  if n not in pair:
    pair.append( n )

print( pair )
