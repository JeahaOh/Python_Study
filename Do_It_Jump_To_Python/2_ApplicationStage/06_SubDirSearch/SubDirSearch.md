# 하위 디렉토리 검색하기
특정 디렉토리부터 시작해서 그 하위 모든 파일 중 `*.py` 파일만 출력해 주는 프로그램을 만드려면 어떻게 해야 할까?  
  
1. SubDirSearch.py 파일을 작성 해 보자.
    ```
      # coding: utf-8
      def search( dirname ):
        print( dirname )

      search( '/' )
    ```
2. 디렉토리에 있는 파일을 검색할 수 있도록 소스를 수정해 보자.
    ```
      # coding: utf-8
      import os


      def search( dirname ):
        filenames = os.listdir( dirname )
        
        for filename in filenames:
          full_filename = os.path.join( dirname, filename )
        
          print( full_filename )

      search( 'c:/' )
    ```
    `os.listdir()`을 사용하면 해당 디렉토리에 있는 파일의 리스트를 구할 수 있다.  
    여기에서 구하는 파일 리스트는 파일 이름만 포함 되어 있으므로,  
    경로를 포함한 파일 이름을 구하기 위해서는 입력 받은 dirname을 앞에 덧붙여 주어야 한다.  
    os 모듈에는 디렉토리와 파일 이름을 이어 주는 `os.path.join()`를 사용하면 디렉토리를 포함한 전체 경로를 쉽게 구할 수 있다.  
  
3. 이제 `c:/` 디렉토리에 있는 파일들 중 확장자가 .py인 파일만을 출력하도록 코드를 변경해 보자.
    ```
      # coding: utf-8
      import os


      def search( dirname ):
        filenames = os.listdir( dirname )
        
        for filename in filenames:
          full_filename = os.path.join( dirname, filename )
          
          ext = os.path.splitext(full_filename)[-1]
          if ext == '.py':
            print( full_filename )

          
      search( 'c:/' )
    ```
    파일 이름에서 확장자만 추출하기 위해 os모듈의 os.path.splitext()를 사용했다.  
    os.path.splitext()는 파일 이름을 확장자 기준으로 두 부분으로 나누어 준다.  
    따라서 ox.path.splitext( full_filename )[-1]은 해당 파일의 확장자 이름이 된다.  
    위 코드는 확장자 이름이 .py인 경우만 출력 하도록 작성했다.  
    `c:/` 디렉토리에 파이썬 파일이 없다면 아무것도 출력되지 않을 것이다.  
  
4. `c:/` 디렉토리뿐만 아니라 그 하위 디렉토리를 포함한 모든 파이썬 파일을 검색 하고 싶다.  
    하위 디렉토리까지 검색 가능하도록 다시 코드를 변경.
    ```
      # coding: utf-8
      import os


      def search( dirname ):
        try:
          filenames = os.listdir( dirname )
          
          for filename in filenames:
            full_filename = os.path.join( dirname, filename )
            if os.path.isdir( full_filename ):
                search( full_filename )
            else:
              ext = os.path.splitext(full_filename)[-1]
              if ext == '.py':
                print( full_filename )
        except PermissionError:
          pass
        except:
          pass

          
      search( 'c:/' )
    ```
    try ... except PermissionError로 함수를 감싼 이유는  
    os.listdir()를 수행할 때 권한이 없는 디렉토리로 접근하더라도 프로그램이 오류로 종료되지 않고 수행되도록 하기 위해서이다.  
      
    full_filename이 디렉토리인지 파일인지 구별하기 위해 os.path.isdir()를 사용하였고,  
    디렉토리일 경우 해당 경로를 입력받아 다시 search()를 호출하였다.  
      
    이렇게 해당 디렉토리의 파일이 디렉토리일 경우 다시 search()를 재귀호출해 나가면  
    해당 디렉토리의 하위 파일을 다시 검색하기 시작하므로 결국 모든 파일들을 검색할 수 있게 된다.  