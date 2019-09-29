# coding: utf-8
'''
range( [start, ] stop[, step] )
입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴
'''
# 인자가 하나인 경우
print( range( 5 ) )

# 인자가 두개인 경우 시작 숫자와 끝 숫자를 나타낸다.
print( range( 5, 10 ) )

# 인자가 세개인 경우 시작과 끝 사이의 거리를 의미한다.
print( range( 5, 10, 2 ) )