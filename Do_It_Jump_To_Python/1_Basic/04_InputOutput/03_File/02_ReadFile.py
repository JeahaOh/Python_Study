# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

f = open('NewFile.txt', 'r')

# readline()은 파일을 한줄씩 읽는다.
# 더 이상 읽을 줄이 없다면 None을 리턴한다.
title( ' readline()로 파일 읽기 ')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line)

# readlines()는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 리턴한다
title( ' readlines() 사용하기')
# lines = f.readlines()
# print( lines )
# for line in lines:
#   print( line )

# read()는 파일의 내용 전체를 문자열로 돌려준다.
title( ' read() 사용하기 ' )
data = f.read()
print( data )

f.close()