# coding: utf-8
'''
# 하위 디렉토리 검색을 쉽게 해 주는 os.walk
os.walk를 사용하면 예제에서 작성한 코드보다 간편하게 만들 수 있다.
os.walk는 시작 디렉토리부터 시작하여 그 하위 모든 디렉토리를 차례대로 방문하게 해 주는 함수이다.

디렉토리와 파일을 검색하는 일반적인 경우라면 os.walk()를 사용하는게 낫다.
'''
import os

for ( path, dir, files ) in os.walk( 'c:/' ):
  for filename in files:
    ext = os.path.splitext( filename )[-1]
    if ext == '.md':
      print( '%s/%s' % (path, filename) )