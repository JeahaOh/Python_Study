# 패키지 안의 함수 실행하기
패키지를 사용하여 echo.py 파일의 echo_test 함수를 실행해 보자.  
패키지 안의 함수를 실행하는 방법은 3가지가 있다.  
다음 예제는 import 예제이므로 하나의 예제를 실행하고나서 다음 예제를 실행할 때는 반드시 인터프리터를 종료하고 다시 실행하도록 하자.  
인터프리터를 다시 시작하지 않을 경우 이전에 import한 것들이 메모리에 남아 있어 엉뚱한 결과가 나올 수 있다.  
1. echo 모듈을 import 하여 실행하는 방법으로 다음과 같이 실행한다.
```
>>> import game.sound.echo
>>> game.sound.echo.echo_text()
echo
```
2. echo 모듈이 있는 디렉토리까지를 from ... import하여 실행하는 방법.
```
>>> from game.sound import echo
>>> echo.echo_test()
echo
```
3. echo 모듈의 echo_text()를 직접 import하여 실행하는 방법이다.
```
>>> from game.sound.echo import echo_text
>>> echo_test()
echo
```
4. 다음과 같이 echo_test()를 사용하는 것은 불가능하다.
```
>>> import game
>>> game.sound.echo.echo_test()
AttributeError: 'module' object has no attribute 'sound'
```
  - import game을 수행하면 game 디렉토리의 모듈 또는 game 디렉토리의 `__init__.py`에 정의한 것만 참조할 수 있다.
5. 다음과 같은 방법도 불가능하다.
```
import game.sound.echo.echo_text
ImportError: No module named echo_test
```
  - .을 사용해서 import a.b.c 처럼 import할 때 가장 마지막 항목이 c는 반드시 모듈 또는 패키지여야 한다.


```
➜  ~ clear
➜  ~ set PYTHONPATH=/Users/Jeaha/game
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
>>>
[1]  + 20768 suspended  python
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from game.sound from echo
  File "<stdin>", line 1
    from game.sound from echo
                       ^
SyntaxError: invalid syntax
>>> from game.sound import echo
>>> echo.echo_test
<function echo_test at 0x109795050>
>>> echo.echo_test()
echo
>>>
[2]  + 21356 suspended  python
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
>>>
[3]  + 22067 suspended  python
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import game
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'sound'
>>>
[4]  + 22599 suspended  python
➜  ~ python
Python 2.7.10 (default, Feb 22 2019, 21:55:15)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import game.sound.echo.echo_test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named echo_test
```