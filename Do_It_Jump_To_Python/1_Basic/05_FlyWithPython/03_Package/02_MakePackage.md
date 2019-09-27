# 패키지 만들기
패키지 기본 구성요소 준비하기.  
다음과 같은 구조로 game 및 기타 서브 디렉토리를 생성하고, .py파일을 만들어 보자.  
1.  
```
game/
    __init__.py
    sound/
          __init__.py
          echo.py
    graphic/
          __init__.py
          render.py
```
2. `__init__.py`파일은 일단 비워둔다.  
3. 
```
# echo.py
# coding: utf-8
def echo_test():
  print( 'echo' )
```
4. 
```
# render.py
# coding: utf-8
def render_test():
  print( 'render' )
```
5. - game 패키지를 참조할 수 있도록 terminal에서 set 명령어로 `PYTHONPATH` 환경 변수에 game 디렉토리를 추가한다.
  - 그리고 Python Interactive Shell을 실행한다.


