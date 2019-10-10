# 간단한 메모장 만들기
원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장을 만들어 보자.  
  
- 필요한 기능은? 메모추가하기, 메모 조회하기
- 입력 받는 값은? 메모 내용, 프로그램 실행 옵션
- 출력하는 값은? 'memo.txt'
  
가장 먼저 해야 할 일은 메모를 추가하는 것이다.  
다름 명령을 실행했을 때 메모를 추가할 수도 있도록 만들어 보자.  
```
  python memo.py -a "Life is too short,"
```
memo.py는 작성할 파이썬 프로그램 이름.  
-a 는 이 프로그램의 실행 옵션.  
"Life is too short,"는 메모에 추가할 내용이 된다.  
  

1. 우선 다음과 같이 입력으로 받은 옵션과 메모를 출력하는 코드를 작성하자.  
    ```
      import sys

      option = sys.argv[1]
      memo = sys.argv[2]

      print( option )
      print( memo )
    ```
    sys.argv는 프로그램을 실행할 때 입력된 값을 읽어 들일 수 있는 파이썬 lib이다.  
    sys.argv[0]은 입력받은 값 중에서 파이썬 프로그램 이름인 memo.py이므로 필요 없는 값이다.  
    그리고 순서대로 sys.argv[1]은 프로그램 실행 옵션 값이 되고,  
    sys.argv[2]는 메모 내용이 된다.  
  
2. 다음 명령을 수행해 보자.  
    ```
      python memo.py -a "Life is too short,"
    ```
    입력으로 전달한 옵션과 메모 내용이 그대로 출력되는 것을 확인할 수 있다.  

3. 입력으로 받은 메모를 파일에 쓰도록 코드를 변경 해 보자.
    ```
      import sys

      option = sys.argv[1]

      if option == '-a':
        memo = sys.argv[2]
        f = open( 'memo.txt', 'a' )
        f.write( memo )
        f.write( '\n' )
        f.close()
    ```
    옵션이 -a인 경우에만 memo 값을 읽어 memo.txt 파일에 그 값을 쓰도록 작성했다.  
    여기에서 매모는 항상 한 줄씩 추가되어야 하므로 파일열기 모드를 a로 했다.  
    그리고 메모를 추가할 때마다 다음 줄에 저장되도록 줄바꿈 문자 `\n`을 추가로 파일에 쓰게 했다.

4. 다음 명령을 수행하자.
    ```
      python memo.py -a "Life is too short,"
      python memo.py -a "You need python."
    ```
    그리고 파일에 정상적으로 메모가 기입 되었는지 확인해 보자.  

5. 작성한 메모를 출력하는 부분을 만들어 보자.  
    메모 출력은 다름과 같이 동작하도록 만들어 보자
    ```
      python memo.py -v
    ```
    메모 추가는 -a 옵션을 사용하고,  
    메모 출력은 -v 옵션을 사용한다.  
    
    다음과 같이 코드를 변경 하도록 하자.
    ```
      import sys

      option = sys.argv[1]

      if option == '-a':
        memo = sys.argv[2]
        f = open( 'memo.txt', 'a' )
        f.write( memo )
        f.write( '\n' )
        f.close()
      elif option == '-v':
        f = open( 'memo.txt' )
        memo = f.read()
        f.close()
      print( memo )
    ```
    옵션으로 -v가 들어온 경우 memo.txt파일을 읽어서 출력한다.

6. 코드를 수정한 후 다음과 같은 명령어를 수행해 보자.
    ```
      python memo.py -v
    ```
