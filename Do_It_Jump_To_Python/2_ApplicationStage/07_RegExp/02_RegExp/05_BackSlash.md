# Back Slash 문제
정규 표현식을 파이썬에서 사용할 때 혼란을 주는 요소가 있는데 바로 `\`이다.  
에를 들어 어떤 파일 안에 있는 `\section` 문자열을 찾기 위한 정규식을 만든다고 가정해 보자.  
  
`\section` 이 정규식은 `\s`문자가 whitespace로 해석되어 의도한 대로 매치가 이루어 지지 않는다.  
위 표현은 `[ \t\n\r\f\v]ection`과 같은 의미이다.  
  
의도한 대로 매치하고 싶다면 `\\section`과 같이 변경해야 한다.  
  
즉, 위 정규식에서 사용한 `\`문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.  
따라서 위 정규식을 컴파일 하려면 다음과 같이 작성 해야 한다.  
  
```
p = re.compile( '\\section' )
```
  
그런데 여기에 또 하나의 문제가 있다.  
이 처럼 정규식을 만들어서 컴파일 하면 실제 파이썬 정규식 엔진에는 파이썬 문자열 리터럴 규칙에 따라  
`\\`이 `\`로 변경되어 `\section`으로 전달 된다.  
  
```
이 문제는 위와 같은 정규식을 파이썬에서 사용할 때만 발생한다.(파이썬의 리터럴 규칙.)
유닉스의 grep, vi 등에서는 이러한 문제가 없다.
```
  
결국 정규식 엔진에 `\\` 문자를 전달하려면 `\\\\`처럼 백슬래시를 4개나 사용해야 한다.  
  
```
정규식 엔진은 정규식을 해석하고 수행하는 모듈이다.
```
  
```
p = re.compile( '\\\\section' )
```
  
만약 위와 같이 `\`를 사용한 표현이 계속 반복되는 정규식이라면 복작해질 것이다.  
이러한 문제로 인한 파이썬 정규식에는 Raw String 규칙이 생겼다.  
즉, 컴파일 해야하는 정규식이 Raw String임을 알려줄 수 있도록 다음과 같은 파이썬 문법을 만든 것이다.  
  
```
p = re.compile(r'\\section' )
```
  
위와 같이 정규식 문자열 앞에 r 문자를 삽입하면  
정규식은 이 Raw String 규칙에 의해 백슬래시 2개 대신 1개만 써도 2개를 쓴것과 동일한 의미를 갖게 된다.  
  
```
만약  백슬래시를 사용하지 않는 정규식 이라면 r의 유무에 상관 없이 동일한 정규식이 될 것이다.
```