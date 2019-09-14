# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' while문의 기본 구조 ')

treeHit = 0
while treeHit < 10:
  treeHit += 1
  print('나무를 %d번 찍었습니다.' % treeHit)
  if treeHit == 10:
    print('나무 넘어갑니다.')

title( ' while문 만들기 ')
prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter Number : '''
no = 0
while no != 4:
  print(prompt)
  no = int( input() )