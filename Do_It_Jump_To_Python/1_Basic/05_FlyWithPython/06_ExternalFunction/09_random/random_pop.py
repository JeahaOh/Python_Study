# coding: utf-8
import random
"""
def random_pop( data ):
  n = random.randint( 0, len( data ) - 1 )
  return data.pop( n )
"""
'''
5
3
1
4
2
리스트의 요소중에서 무작위로 하나를 선택하여 꺼낸 값을 리턴.

random.choice()를 사용하면 더 직관적으로 만들 수 있다.
random.choice()는 입력으로 받은 리스트에서 무작위로 하나를 선택해서 리턴.
'''
def random_pop( data ):
  n = random.choice( data )
  data.remove( n )
  return n
'''
1
4
2
3
5
'''

if __name__ == '__main__':
  data = [1, 2, 3, 4, 5]
  while data:
    print( random_pop( data ) )

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.suffle()를 이용하면 된다.
data = [1, 2, 3, 4, 5]
random.shuffle( data )
print( data )