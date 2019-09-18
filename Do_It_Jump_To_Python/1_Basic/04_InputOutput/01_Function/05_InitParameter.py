# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 매개변수에 초깃값 미리 설정하기 ' )
def intruduce_myself( name, old, work=True ):
  print("I'm %s." % name )
  print("I'm %d age old." % old )
  if work:
    print("I'm on work.")
  else:
    print("I'm out of work.")
  print('')

intruduce_myself( 'Jeaha', 28)
intruduce_myself( '백수', 28, False)

'''
매개변수에 미리 값을 넣어, 매개변수의 초기값을 설정하는 방법이다.
매개변수의 값이 항상 변하는 것이 아닐 경우 이렇게 초기값을 미리 설정해 둘 수 있다.
초기화시키고 싶은 매개변수는 항상 뒤쪽에 두도록 하자.
'''