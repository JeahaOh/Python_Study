# 패키지란?
Package는 .(도트)를 사용해서 파이썬 모듈을 계층적(디렉토리 구조)으로 관리할 수 있개 한다.  
예를 들어,  
모듈 A.B인 경우 :  
A는 패키지 이름이 되고  
B는 A패키지의 모듈이 된다.  
  
### 가상의 game 패키지 예 :
```
game/
    __init__.py
    sound/
          __init__.py
          echo.py
          wav.py
    graphic/
          __init__.py
          screen.py
          render.py
    play/
          __init__.py
          run.py
          test.py
```
game, sound, graphic, play는 디렉토리 이름이고, 확장자가 .py인 파일은 파이썬 모듈이다.  
gmae 디렉토리가 이 패키지의 루트 디렉토리이고,  
sound, graphic, play는 서브 디렉토리이다.  
  
간단한 프로그램이 아니라면 이렇게 패키지 구조로 프로그램을 만드는 것이 공동 작업이나 유지보수 등 여러면에서 유리하다.  
또한 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.  

### __init__.py
파일은 특별한 용도로 사용함.  
뒤에서 자세하게 알아보도록 하자.  
