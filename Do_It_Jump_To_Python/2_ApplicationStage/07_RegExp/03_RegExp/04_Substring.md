# 문자열 바꾸기
sub 메소드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.  
```
>>> p = re.compile( '(blue|white|red)' )
>>> p.sub( 'coluor', 'blue socks and red shoes' )
'coluor socks and coluor shoes'
```
sub 메소드의 첫 번째 매개변수는 '바꿀 문자열(replacement)'이 되고,  
두 번째 매개변수는 '대상 문자열'이 된다.
  
바꾸기 횟수를 제어하고 싶다면 다음과 같이 세 번째 매개변수로 count 값을 넘기면 된다.  
```
>>> p.sub( 'coluor', 'blue socks and red shoes', count=1 )
'coluor socks and red shoes'
```
  
sub과 동일한 기능을 하지만 반환 결과를 튜플로 돌려주는 subn()도 있다.  
돌려준 튜플의 첫 번째 요소는 변경된 문자열 이고, 두 번째 요소는 바꾸기가 발생한 횟수이다.
```
>>> p.subn( 'coluor', 'blue socks and red shoes', count=1 )
('coluor socks and red shoes', 1)
```
  
## sub() 사용 시 참조 구문 사용하기
```
>>> p = re.compile( r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)' )
>>> print( p.sub( '\g<phone> \g<name>', 'ASDF 010-1234-1234' ) )
010-1234-1234 ASDF
```
  
`이름 + 문자열`의 문자열을 `전화번호 + 이름`으로 바꾸는 예이다.  
sub의 바꿀 문자열 부분에 `\g<그룹 이름>`을 사용하면 정규식의 그룹 이름을 참조할 수 있게 된다.  
다음과 같이 그룹 이름 대신 참조 번호를 사용해도 마찬가지 결과를 돌려준다.  
```
>>> p = re.compile( r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)' )
>>> print( p.sub( '\g<2> \g<1>', 'ASDF 010-1234-1234' ) )
010-1234-1234 ASDF
```
  
## sub()의 매개변수로 함수 넣기
sub()의 첫 번째 매개변수로 함수를 넣을 수도 있다.  
```
>>> def hexrepl( match ):
...     value = int( match.group() )
...     return hex( value )
... 
>>> p = re.compile( r'\d+' )
>>> p.sub( hexrepl, 'Call 12345 for printing, 23456 for user code.' )
'Call 0x3039 for printing, 0x5ba0 for user code.'
```
hexrepl 함수는 match 객체(위에서 숫자에 매치되는)를 입력으로 받아 16진수로 변환하여 돌려주는 함수이다.  
sub의 첫 번째 매개변수로 함수를 사용할 경우 해당 함수의 첫 번째 매개변수에는 정규식과 매치된 match 객체가 입력된다.  
그리고 매치되는 문자열은 함수의 반환 값으로 바뀌게 된다.  
  
