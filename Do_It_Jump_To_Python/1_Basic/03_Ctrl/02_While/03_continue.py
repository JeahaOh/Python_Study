# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' while문의 맨 처음으로 돌아가기 ')
a = 0
while a < 10:
  a += 1
  if a % 2 == 0 : continue
  print( a )

while True:
  title( ' 무한루프는 "CTRL + C"를 눌러야 탈출할 수 있다 냥. ' )
