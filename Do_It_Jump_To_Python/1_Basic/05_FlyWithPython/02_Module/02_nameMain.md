# if __name__ == "__main__"의 의미
mod1.py를 다음과 같이 수정  
```
def add( a, b ):
  return a + b
def sub( a, b ):
  return a - b

print( add( 1, 4 ) )
print( sub( 4, 2 ) )
```
  
수정 후 모듈을 import하면
```
>>> import mod1
5
2
```
  
import를 하는 순간 mod1.py가 실행되면서 결과 값이 출력 됨.  
이런 문제를 방지하기 위해 파일을 다음과 같이 바꿈.  
```
def add( a, b ):
  return a + b
def sub( a, b ):
  return a - b

if __name__ == "__main__":
  print( add( 1, 4 ) )
  print( sub( 4, 2 ) )
```
  
##  
`if __name__ = "__main__"`를 사용하면,
이 파일을 직접 실행했을 때는 `if __name__ = "__main__"`이 참이 되어 if문 다음 문장이 수행됨.  
이 파일을 모듈을 불러와 사용할 때는 거짓이 되어 if문 다음 문장이 실행되지 않고 모듈로 import 됨.

## __name__
`__name__` 변수는 Python이 내부적으로 사용하는 특별한 변수 이름임.  
`*.py` 파일을 직접 실행할 경우 `*.py`의 `__name__` 변수에는 `__main__` 값이 저장되어 있음.  
`*.py` 파일을 모듈로 import 할 경우 `__name__` 변수에는 모듈의 이름 값 `*`이 저장되어 있음.  