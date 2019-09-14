# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)
title( ' elif ' )
# python에서는 else if를 elif로 사용함.
# 주머니에 돈이 있으면 택시를 타고,
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고,
# 돈도 카드도 없으면 걸어서 가라
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
  print( ' TAXI 1 ')
else:
  if card:
    print( ' TAXI 2 ')
  else:
    print( ' WALK ' )

if 'money' in pocket:
  print( ' TAXI 1 ' )
elif card:
  print( ' TAXI 2 ' )
else:
  print( ' WALK ')

title( ' 한줄로 작성하기 ')
if 'money' not in pocket: pass
else: print(' Card ')