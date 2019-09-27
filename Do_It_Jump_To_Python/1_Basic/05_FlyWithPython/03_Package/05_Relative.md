# relative 패키지
graphic 디렉토리의 render.py 모듈이 sound 디렉토리의 echo.py 모듈을 사용하고 싶다면,  
다음과 같이 render.py를 수정하면 가능하다.
```
# coding: utf-8
from game.sound.echo import echo_test

def render_test():
  print( 'render' )
  echo_test()
```
`from game.sound.echo import echo_test` 문장을 추가하여 echo_test()를 사용 할 수 있도록 수정한다.
```
>>> from game.graphic.render import render_test
>>> render_test()
render
echo
```

`from game.graphic.render import render_test`를 입력해 전체 경로를 사용하여 import할 수도 있지만 relative 하게 import하는 것도 가능하다.
```
# coding: utf-8
from ..sound.echo import echo_test

def render_test():
  print( 'render' )
  echo_test()
```

`from game.graphic.render import render_test`가  
`from ..sound.echo import echo_test`로 변경되었다.  
여기서 `..`은 부모 디렉토리를 의미한다.  
graphic과 sound 디렉토리는 동일한 깊이(depth)이므로 부모 디렉토리 `..`를 사용하여 위와같은 import가 가능하다.  
  
relative한 접근자에는 다음과 같은 것이 있다.
- `..` : 부모 디렉토리
- `.`  : 현재 디렉토리
relative한 접근자는 render.py처럼 모듈 안에서만 사용해야 한다.  
파이썬 인터프리터에서 relative한 접근자를 사용하면  
`SystemError: connot perform relative import` 오류가 발생한다.