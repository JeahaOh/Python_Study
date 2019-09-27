# __init__.py의 용도
`__init__.py` 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다.  
만약 game, sound, graphics 등 패키지에 포함된 디렉토리에 `__init__.py` 파일이 없다면 패키지로 인식되지 않는다.  
python3.3버전 부터는 `__init__.py` 파일이 없어도 패키지로 인식한다.  
하지만 하위호환을 위해 생성하는 것이 안전한 방법이다.  
  
다음을 따라하자.
```
>>> from game.sound import *
>>> echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined
```
game.sound 패키지의 모든것( * )을 import하였지만 echo라는 이름이 정의 되지 않았다는 에러가 뜬다.  
이렇게 특정 디렉토리의 모듈을 ( * )을 사용하여 import할 때는 다음과 같이 해당 디렉토리의 `__init__.py` 파일에 `__all__` 변수를 설정하고 import할 수 있는 모듈을 정의해 주어야 한다.  
```
# game/sound/__init__.py
__all__ = ['echo']
```
여기서 `__all__`이 의미하는 것은 sound 디렉토리에서 * 기호를 사용해서 import할 경우 이곳에 정의된 echo 모듈만 import 된다는 의미이다.  
  
`__init__.py` 파일을 변경한 후 위 예제를 수행하면 원하던 결과가 출력될 것이다.

```
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from game.sound import *
>>> echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined
>>>
KeyboardInterrupt
>>>
[6]  + 25604 suspended  python
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from game.sound import *
>>> echo.echo_test()
echo
```
## 
착각하기 쉬운데 `from game.sound.echo import *`은 `__all__`과 상관없이 무조건 import 된다.  
이렇게 `__all__`과 상관없이 무조건 import되는 경우는  
`from a.b.c import *`에서 from의 마지막 항목인 c가 모듈인 경우이다.

