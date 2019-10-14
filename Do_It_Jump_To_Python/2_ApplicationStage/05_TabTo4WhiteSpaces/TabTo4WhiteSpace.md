# 탭을 4개의 공백으로 바꾸기
문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을 공백(space) 4개로 바꾸는 스크립트를 작성해 보자.  
  
- 필요한 기능? 문서 파일 읽어 들이기, 문자열 변경하기
- 입력 받는 값은? 탭을 포함한 문서 파일
- 출력하는 값은? 탭이 공백으로 수정된 문서 파일
  
다음과 같은 형식으로 프로그램이 수행되도록 만들 것이다.
```
python tabto4.py src dst
```
  
tabto4.py는 파이썬 프로그램 이름.  
src는 탭을 포함하고 있는 원본 파일 이름.  
dst는 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 파일 이름.  
  
a.txt 파일에 있는 탭을 공백 4개로 바꾸어 b.txt 파일에 저장하고 싶다면 다음과 같이 수행해야 한다.  
```
python tabto4.py a.txt b.txt
```
  
1. 우선 다음과 같이 tabto4.py 파일을 작성해 보자.
    ```
      # coding: utf-8
      import sys

      src = sys.argv[1]
      dst = sys.argv[2]

      print( src )
      print( dst )
    ```
    sys.argv를 통해 입력 값을 확인하도록 만든 코드이다.

2. 다음과 같이 수행했을 때 입력 값이 정상적으로 출력되는지 확인해 보자.
    ```
      PS C:\05_TabTo4WhiteSpaces> python tabto4.py a.txt b.txt
      a.txt
      b.txt
    ```
    입력 값으로 전달한 a.txt와 b.txt가 정상적으로 출력되는 것을 확인할 수 있다.

3. 테스트를 위한 원본 파일인 a.txt를 다음과 같이 작성한다.
    ```
      Life    is    too   short,
      You    need    Python.
    ```

4. 탭 문자를 포함한 a.txt 파일을 읽어서 탭을 공백 4개로 변환할 수 있도록 코드를 변경하자.
    ```
      # coding: utf-8
      import sys

      src = sys.argv[1]
      dst = sys.argv[2]

      f = open( src )
      tab_content = f.read()
      f.close()

      space_content = tab_content.replace( '\t', ' ' * 4 )
      print( space_content )
    ```
    src에 해당되는 입력 파일을 읽어서 그 내용을 tab_content라는 변수에 저장 후,  
    문자열의 replace 함수를 사용하여 `\t`을 공백 4개로 변경하는 코드이다.

5. tabto4.py를 실행해 보자.
    ```
      PS C:\05_TabTo4WhiteSpaces> python tabto4.py a.txt b.txt
      Life    is      too     short,
      You     need    Python.
    ```
    탭과 공백의 차이점을 눈으로 할 수 없으므로 정상적으로 탭이 공백으로 변경되었는지 확인하기 어렵다.

6. 변경된 내용을 b.txt 파일에 저장할 수 있도록 프로그램을 수정한다.
    ```
      # coding: utf-8
      import sys

      src = sys.argv[1]
      dst = sys.argv[2]

      f = open( src )
      tab_content = f.read()
      f.close()

      space_content = tab_content.replace( '\t', ' ' * 4 )
      f = open( dst, 'w')
      f.write( space_content )
      f.close()
    ```

7. 프로그램을 실행하면 b.txt 파일이 디렉토리에 생성된다.