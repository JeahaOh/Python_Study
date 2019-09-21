# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

# with를 사용하면 with 블록을 벗어나는 순간, 열린 파일 객체가 자동으로 close 된다.

with open('with.md', 'w') as f:
  f.write( '# Life is too short, You need Python.')