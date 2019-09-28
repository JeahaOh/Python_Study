# Exception Handling

# try, except
오류 처리를 위한 try, except문의 기본 구조
```
try:
  ...
except[ 발생오류 [as 오류 메세지 변수] ]:
  ...
```

try 블럭 수행 중 오류가 발생하면 except 블럭이 수행된다.
try 블럭에서 오류가 발생하지 않는다면 except 블럭은 수행되지 않는다.

1. try, except 만 쓰는 방법  
  예외의 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.
    ```
      try:
        ...
      except:
        ...
    ```
2. 발생 오류만 포함한 except 문  
  오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다.
    ```
      try:
        ...
      except 발생 오류:
        ...
    ``` 
3. 발생 오류와 오류메세지 변수까지 포함한 except문  
  이 경우는 두 번째 경우에서 오류 메세지의 내용까지 알고 싶을 때 사용하는 방법이다.
    ```
      try:
        ...
      execpt 발생 오류 as 오류 메세지 변수:
        ...
    ```
    ```
      try:
        4 / 0
      except ZeroDivisionError as e:
        print( e )    //  integer division or modulo by zero
    ```
4. finally  
  try 문은 오류 발생 여부와 상관없이 항상 수행된다.  
  보통 사용한 리소스를 close할 때 사용한다.
    ```
      f = open( 'asdf.txt', 'w' )
      try:
        ...
      finally:
        f.close()
    ```
5. 여러개의 오류 처리하기  
  try 문 안에서 여러개의 오류를 처리하기 위해 다음과 같이 쓸 수 있다.
    ```
      try:
        ...
      except 발생 오류 1:
        ...
      except 발생 오류 2:
        ...
    ```
    ```
      try:
        ...
      except 발생 오류 1 as 오류 메세지 변수:
        ...
      except 발생 오류 2 오류 메세지 변수:
        ...
    ```
    ```
      try:
        ...
      except (발생 오류 1, 발생 오류 2) as 오류 메세지 변수:
        ...
    ```