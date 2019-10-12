# match 객체의 메소드
match()와 search()를 수행한 결과로 돌려준 match 객체에 대해서 알아보자.  
match 객체에는 다음과 같은 메소드 들이 있다.  
|**method**|목적|
|---|---|
| group() | 매치된 문자열을 리턴.|
| start() | 매치된 문자열의 시작 위치를 리턴.|
| end()   | 매치된 문자열의 끝 위치를 리턴.|
| span()  | 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴.|
다음 예로 확인해 보자.  
  
```
>>> m = p.match( 'python' )
>>> m.group()
'python'
>>> m.start()
0
>>> m.end()
6
>>> m.span()
(0, 6)
```
  
match()의 수행 결과로 반환 받은 match 객체의 start() 값은 항항 0일 수 밖에 없다.  
만약 search()를 사용한다면 start()의 값은 다음과 같이 다르게 나올 것이다.  
  
```
>>> m = p.search( '3 python' )
>>> m.group()
'python'
>>> m.start()
2
>>> m.end()
8
>>> m.span()
(2, 8)
```
  
## 모듈 단위로 수행하기
앞에서는 `re.compile()`을 사용하여 컴파일한 패턴 객체로 그 이후의 결과를 수행했지만,  
re 모듈은 이것을 축약한 형태로 사용할 수 있는 방법을 제공한다.  
  
```
>>> p = re.compile( '[a-z]+' )
>>> m = p.match( 'python' )
```
  
위 코드를 축약하면 다음과 같다.
  
``` 
>>> m = re.match( '[a-z]+', 'python' )
```
  
위 예처럼 사용하면 compile()과 match()를 한 번에 수행할 수 있다.  
보통 한 번 만든 패턴 객체를 여러번 사용해야 할 경우에는 `re.compile()`을 사용하는 것이 편하다.