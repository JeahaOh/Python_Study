# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

f = open('NewFile.txt', 'a')

'''
파일에 새로운 내용 추가하기
원래 있던 값을 유지하면서 새로운 값만 추가해야할 경우 a 모드로 연다.
'''
for i in range(11, 21):
  data = 'Line %d : \n' % i
  f.write( data )

f.close()