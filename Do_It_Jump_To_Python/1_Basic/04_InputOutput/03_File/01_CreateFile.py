# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 파일 생성하기 ' )
f = open('NewFile.txt', 'w')
for i in range( 1, 11 ):
  data = 'Line %d : \n' % i
  f.write(data)

'''
파일을 생성하기 위해 파이썬 내장함수 open을 사용했다.

파일 객체 = open( 파일이름, 파일 열기 모드 )
r = 읽기 전용
w = 쓰기 모드
a = 파일의 마지막에 새로운 내용 추가

close() 파일을 닫음.
'''

f.close()