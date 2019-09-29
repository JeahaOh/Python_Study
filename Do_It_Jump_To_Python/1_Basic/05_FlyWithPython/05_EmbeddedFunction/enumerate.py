# coding: utf-8
'''
enumerate( x )
순서가 있는 자료형을 입력 받아 인덱스 값을 포함하는 tuple 객체(?)를 반환
'''
for i, name in enumerate( ['Life', 'is', 'Python']):
  print i, name 
  print( type( ( i, name ) ) )

'''
enumerate를 for문과 사용하면 자료형의 index와 값을 알 수 있다.
반복 되는 구간에서 객체가 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 유용.
'''