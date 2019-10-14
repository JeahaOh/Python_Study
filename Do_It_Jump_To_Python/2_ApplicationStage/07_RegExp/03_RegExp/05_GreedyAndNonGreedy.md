# Greedy vs Non-Greedy
정규식에서 Greedy란  
```
>>> s = '<html><head><title>Title</title>'
>>> len( s )
32
>>> print( re.match( '<.*>', s ).span() )
(0, 32)
>>> print( re.match( '<.*>', s ).group() )
<html><head><title>Title</title>
```
`<.*>` 정규식의 매치 결과로 `<html>` 문자열만 돌려주기를 원하지만,  
`*` 메타문자는 매치할 수 있는 최대한의 문자열인 `<html><head><title>Title</title>` 문자열을 모두 소비해 버렸다.(이것을 탐욕스럽다고 표현 한다.)  
다음과 같이 non-greedy 문자인 `?`를 사용하면 `*`의 탐욕을 제한할 수 있다.  
```
>>> print( re.match( '<.*?>', s ).group() )
<html>
```
non-greedy 문자인 `?`는 `*?`, `+?`, `??`, `{m, n}`과 같이 사용할 수 있다.  
가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.