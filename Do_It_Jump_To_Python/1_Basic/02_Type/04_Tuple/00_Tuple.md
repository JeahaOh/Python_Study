# Tuple
튜플은 리스트와 거의 비슷하며 다른점은 다음과 같다.  
- 리스트는 []으로 둘러싸지만, 튜플은 ()로 둘러 싼다.
- 리스트는 값의 생성, 삭제, 수정이 가능하지만, 튜플은 바꿀 수 없다.

## 튜플의 모습
```
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
```
리스트와 거의 비슷한 모습이지만, 두가지 차이점이 있다.  
1. t2 = (1,)    : 1 개의 요소를 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
2. t4 = 1, 2, 3 : 괄호를 생략해도 무방하다.
  
튜플은 값의 변화가 불가능하기 때문에 리스트와 구분해서 사용해야 한다.  
