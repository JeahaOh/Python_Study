# 컴파일 옵션
  
정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.
- DOTALL( S )     : `.`이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
- IGNORECASE( I ) : 대소문자에 관계없이 매치할 수 있도록 한다.
- MULTILINE( M )  : 여러줄과 매치할 수 있도록 한다.         (`^`, `$` 메타 문자의 사용과 관계가 있는 옵션.)
- VERBOSE( X )    : verbose 모드를 사용할 수 있도록 한다.  (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게 된다.)
옵션을 사용할 때는 `re.DOTALL()` 처럼 전체 옵션 이름을 써도 되고, `re.S` 처럼 약어를 써도 된다.
  

## DOTALL, S
`.` 메타문자는 줄바꿈 문자(`\n`)를 제외한 모든 문자와 매치되는 규칙이 있다.  
만약 `\n` 문자도 포함하여 매치하고 싶다면 `re.DOTALL` 또는 `re.S` 옵션을 사용해 정규식을 컴파일 하면 된다.  
  
```
>>> p = re.compile( 'a.b' )
>>> m = p.match( 'a\nb' )
>>> print( m )
None
```
  
정규식이 `a.b`인 경우 문자열 `a\nb`는 매치되지 않음을 알 수 있다.  
메타문자 `.`가 `\n` 문자와도 매치되게 하려면 다음과 같이 `re.DOTALL` 옵션을 사용하면 된다.  
  
```
>>> p = re.compile( 'a.b', re.DOTALL )
>>> m = p.match( 'a\nb' )
>>> print( m )
<_sre.SRE_Match object at 0x104b4bb90>
```  
  
보통 `re.DOTALL` 옵션은 여러 불로 이루어진 문자열에서 `\n`에 상관 없이 검색할 때 많이 사용한다.  
  

## IGNORECASE, I
`re.IGNORECASE`, `re.I` 옵션은 대소문자 구별 없이 매치를 수행할 때 사용하는 옵션이다.  
  
```
>>> p = re.compile( '[a-z]', re.I )
>>> p.match( 'python' )
<_sre.SRE_Match object at 0x104b4bbf8>
>>> p.match( 'Python' )
<_sre.SRE_Match object at 0x104b4bc60>
>>> p.match( 'PYTHON' )
<_sre.SRE_Match object at 0x104b4bbf8>
```
  
`[a-z]`는 소문자만을 의미하지만 re.I 옵션으로 대소문자 구분 없이 매치된다.
  
## MULTILINE, M
`re.MULTILINE`또는 `re.M` 옵션은 메타문자 `^`, `$`와 연관된 옵션이다.  
간단히 보자면 `^`는 문자열의 처음을 의미하고, `$`는 문자열의 마지막을 의미한다.  
예를 들어 정규식이 `^python`인 경우 문자열의 처음은 항상 python으로 `시작`해야 매치되고,  
만약 정규식이 `python$`인 경우라면 문자열의 마지막은 항상 python으로 `끝`나야 매치된다는 의미다.  
  
```
>>> import re
>>> p = re.compile( '^python\s\w+' )
>>> data = """python one
... life is too short
... python two
... you need python
... python tree"""

>>> print( p.findall( data ) )
['python one']
```
  
메타 문자 `^`에 의해 python이라는 문자열을 사용한 첫 번째 줄만 매치된 것이다.  
하지만 `^`를 전체의 처음이 아니라 각 라인의 처음으로 인식 시키고 싶은 경우 사용하는 옵션이 `re.MULTILINE`, `re.M`이다.  
  
```
>>> data = """python one
... life is too short
... python two
... you need python
... python tree
... """

>>> p = re.compile( '^python\s\w+', re.MULTILINE )

>>> print( p.findall( data ) )
['python one', 'python two', 'python tree']
```
  
`re.MULTILINE` 옵션은 `^`, `$` 메타 문자가 문자열 각 줄마다 적용해 주는 것.
  
## VERBOSE, X
정규 표현식이 복잡해지면 주석을 다는 옵션이다.  
다음 두 예를 보면
```
charerf = re.compile( r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);' )
```
  
```
charref = re.compile( r"""
    &[#]                # Start of a numeric entity reference
    (
      0[0-7]          # Octal form
      | [0-9+           # Decimal form
      | x[0-9a-fA-F]+   # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """, re.VERBOSE )
```
첫 번째와 두 번째 예를 비교해 보면 컴파일 된 패턴 객체인 charref는 모두 동일한 역할을 한다.  
하지만 정규식이 복잡할 경우 두 번째 처럼 주석을 적고 여러 줄로 표현하는 것이 훨씬 가독성이 좋다는 것을 알 수 있다.  
  
`re.VERBOSE` 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일 할 때 제거된다. ([]안에 사용한 whitespace는 제외)  
그리고 줄 단위로 # 기호를 사용하여 주석문을 작성할 수 있다.