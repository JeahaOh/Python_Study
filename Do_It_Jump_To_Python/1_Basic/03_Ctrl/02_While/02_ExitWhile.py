# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' while문 강제로 빠져나가기 break ')

coffee = 10

while True:
  money = int( input('\n돈을 넣어라 냥 : ') )
  
  if money == 300:
    print('커피를 준다 냥.')
    coffee -= 1
  elif money > 300:
    print('거스름돈 %d과 커피를 준다 냥.' % (money - 300))
    coffee -= 1
  else:
    print('돈을 돌려주고  커피를 주지 않는다 냥.')
    print('커피는 300원이고, 남은 커피는 %d개다 냥.' % coffee)
  
  if coffee == 0:
    print('커피가 다 떨어졌다 냥.')
    break
