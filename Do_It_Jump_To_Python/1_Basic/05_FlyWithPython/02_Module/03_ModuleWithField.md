# 클래스나 변수등을 포함한 모듈
모듈은 클래스나 변수등을 포함할 수 있다.
### mod2.py
```
# coding: utf-8
PI = 3.141592

class Math:
  def solv( self, r ):
    return PI * ( r ** 2 )

def add( a, b ):
    return a + b

```
이 파일은 원의 넓이를 구하는 Math 클래스와 두 값을 더하는 add 함수, 그리고 원주윻 값에 해당하는 PI 변수로,  
클래스, 함수, 변수를 모두 포함하고 있다.

```
>>> import mod2
>>> 
>>> print( mod2.PI )
3.141592
```
위처럼 PI 변수의 값을 사용할 수 있다.  
  
```
>>> a = mod2.Math()
>>> print( a.solv( 2 ) )
12.566368
```
모듈 안에 있는 클래스를 사용하려면 `.(도트연산자)`로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다.  
  
  
```
>>> print( mod2.add( mod2.PI, 4.4 ) )
7.541592
>>> 
```
함수 역시 사용 가능하다.