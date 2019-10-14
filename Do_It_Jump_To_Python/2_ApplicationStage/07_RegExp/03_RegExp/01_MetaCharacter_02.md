# Meta Character
`+`, `*`, `[]`, `{}` 등의 메타문자는 매치가 진행될 때 현재 매치가 되고 있는 문자열의 위치가 변경된다.(소비된다고 표현한다)  
이와 달리 문자열을 소비시키지 않는 메타 문자(zerowidth assertions)를 알아보자.  
  
# |
`|` 메타 문자는 or과 같은 의미로 사용된다.  
`A|B`라는 정규식이 있다면, A 또는 B 라는 의미가 된다.  
  
```
>>> p = re.compile( 'Crow|Servo' )
>>> m = p.match( 'CrowHello' )
>>> print( m )
<_sre.SRE_Match object at 0x1072d6b28>
```
  
# ^
`^` 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.  
`re.MULTILINE`을 사용하는 경우에는 여러 줄의 문자열 일 때 각 줄의 처음과 일치하게 된다.  
  
```
>>> print( re.search( '^Life', 'Life is too short' ) )
<_sre.SRE_Match object at 0x1072d6b90>
>>> print( re.search( '^Life', 'My Life' ) )
None
```
`^Life` 정규식은 Life 문자열이 처음에 온 경우에는 매치하지만 처음 위치가 아닌 경우에는 매치 되지 않음을 알 수 있다.  
  
# $
`$` 메타문자는 `^`와 반대로 문자의 끝과 매치함을 의미한다.  
  
```
>>> print( re.search( 'short$', 'Life is too short' ) )
<_sre.SRE_Match object at 0x1072d6b90>
>>> print( re.search( 'short$', 'Life is too short, you need python' ) )
None
```
  
# \A
`\A`는 문자열의 처음과 매치됨을 의미한다. `^` 메타문자와 동일한 의미지만.  
`re.MULTILINE` 옵션을 사용할 경우에는 다르게 해석된다.  
`re.MULTILINE` 옵션을 사용할 경우 `^`는 각 줄의 문자열의 처음과 매치되지만,  
`\A`는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.  
  
# \Z
`\Z`는 문자열의 끝과 매치됨을 의미한다.  
`\A`와 동일하게 `re.MULTILINE` 옵션을 사용할 경우 `$`와 달리 전체 문자열의 끝과 매치된다.  
  
# \b
`\b`는 단어 구분자(Word Boundary)이다. 보통 단어는 whitespace에 의해 구분 된다.
```
>>> p = re.compile( r'\bclass\b' )
>>> print( p.search( 'no class at all' ) )
<_sre.SRE_Match object at 0x1072d6b90>
>>> print( p.search( 'the declassified algorithm' ) )
None
>>> print( p.search( 'one subclass is' ) )
None
```
`\bclass\b` 정규식은 whitespace로 구분된 class라는 단어와 매치됨을 의미한다.  
따라서 `no class at all`의 class라는 단어와 매치 되지만,  
whitespace로 구분 되지 않은 `subclass`나 `declassified`와는 메치되지 않는다.  
  
# \B
`\B`는 `\b`와 반대의 경우이다.  
whitespace로 구분된 단어가 아닌 경우에만 매치된다.  
class 단어 앞뒤에 whitespace가 하나라도 있는 경우에는 매치가 안 된다.  
```
>>> p = re.compile( r'\Bclass\B' )
>>> print( p.search( 'no class at all' ) )
None
>>> print( p.search( 'the declassified algorithm' ) )
<_sre.SRE_Match object at 0x1072d6b90>
>>> print( p.search( 'one subclass is' ) )
None
```