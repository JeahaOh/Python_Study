# coding: utf-8
'''
## Q3 리스트의 더하기와 extend 함수
다음과 같은 리스트 a가 있다.  
```
>>> a = [1, 2, 3]
```
리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.  
  
```
>>> a = [1, 2, 3]
>>> a = a + [4,5]
>>> a
[1, 2, 3, 4, 5]
```
리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.  
  
```
>>> a = [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
```
`+` 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.
'''

# 리스트 a에 +기호를 사용하는 경우
a = [1, 2, 3]
print( id(a) )

a = a + [4, 5]
print( a )
print( id( a ) )

## +기호를 사용하면 리스트 a의 값이 변한것이 아니라 두 리스트가 더해진 새로운 리스트가 반환된다.

# extend 함수를 사용하는 경우
a.extend( [6, 7] )
print( a )
print( id( a ) )

## +기호를 사용한 경우와 달리 주소 값이 변하지 않고 그대로 유지된다.