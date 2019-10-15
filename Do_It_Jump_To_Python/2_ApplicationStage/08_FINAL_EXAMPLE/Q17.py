# coding: utf-8
'''
## Q17 기초 메타 문자
다음 중 정규식 `a[.]{3,}b`과 매치되는 문자열은 무엇일까?  
  
1. `acccb`
2. `a....b`
3. `aaab`
4. `a.cccb`
'''
import re
p = re.compile('a[.]{3,}b')

print( p.match( "acccb" ) )   #
print( p.match( "a....b" ) )  #
print( p.match( "aaab" ) )    #
print( p.match( "a.cccb" ) )  #