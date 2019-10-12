# 파이썬에서 정규 표현식을 지원하는 re 모듈
파이썬은 정규 표현식을 지원하기 위해 re(Regular Expression) 모듈을 제공한다.  
re 모듈은 파이썬을 설치할 때 자동으로 설치되는 기본 라이브러리로 사용법은 다음과 같다.  
```
import re
pattern = re.compile('ab*')
```
re.compile을 사용해 정규표현식을 컴파일 한다.  
re.compile의 결과로 돌려주는 객체(pattern)를 사용하여 그 이후의 작업을 수행할 수 있다.
- 정규식을 컴파일 할 때 특정 옵션을 주는 것도 가능하다.
- 패턴이랑 정규식을 컴파일한 결과이다.

## 정규식을 이용한 문자열 검색
컴파일 된 패턴 객체를 사용하여 문자열 검색을 수행할 수 있다. 패턴 객체는 다음과 같은 4가지 메소드를 데공한다.
| **Method**|**목적**|
|-----------|---|
| match()   | 문자열의 처음부터 정규식돠 매치되는지 조사한다. |
| search()  | 문자열 전체를 검색하여 정규식과 매치되는지 조사한다. |
| findall() | 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴. |
| finditer()| 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다. |
  
match, search는 정규식과 매치될 때는 match 객체를 돌려주고,  
매치되지 않을 때는 None을 돌려준다.  
  
우선 패턴을 만들어 보자.
```
>>> import re
>>> p = re.compile( '[a-z]+' )
```
  
## match
match()는 문자열의 처음부터 정규식과 매치되는지 조사한다.  
위 패턴에 match 메소드를 수행해 보자.  
'python' 문자열은 `[a-z]+` 정규식에 부합되므로 match 객채를 리턴한다.
```
>>> m = p.match( 'python' )
>>> print( m )
<_sre.SRE_Match object at 0x104b4bb28>
```
  
'3 python' 문자열은 `[a-z]+` 정규식에 부합되지 않으므로 None을 돌려준다.  
```
>>> m = p.match( '3 python' )
>>> print( m )
None
```
  
match의 결과로 match 객체 또는 None을 돌려주기 때문에  
결과 값이 있을 경우만 다음 작업을 수행하기 위해 보통 다음과 같은 흐름으로 작성한다.
```
ptn = re.compile( 정규표현식 )
m = ptn.match( 대상 문자열 )

if m:
  print( 'Match found : ', m.group() )
else :
  print( 'No match' )
```
  
## search
컴파일 된 객체 ptn을 가지고 search()를 수행해 보자.
```
>>> m = p.search( 'python' )
>>> print( m )
<_sre.SRE_Match object at 0x104b4bb28>

>>> m = p.search( '3 python' )
>>> print( m )
<_sre.SRE_Match object at 0x104b4bb90>
```
search()는 문자열의 처음부터 검색하는 것이 아니라 문자열 전체를 검색함.  
match()와 search()는 문자열의 처음부터 검색할지의 여부에 따라 다르게 사용해야 한다.
  
## findall
```
>>> result = p.findall( 'life is too short' )
>>> print( result )
['life', 'is', 'too', 'short']
```
findall()는 대상 문자열에서 `[a-z]+` 정규식과 매치해서 리스트로 돌려준다.
  
## finditer
```
>>> result = p.finditer( 'you need python' )
>>> print( result )
<callable-iterator object at 0x104b6f990>
 
>>> for r in result: print( r )
... 
<_sre.SRE_Match object at 0x104b4bb28>
<_sre.SRE_Match object at 0x104b4bbf8>
<_sre.SRE_Match object at 0x104b4bb28>
```
finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다.  
반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.