# 다른 파일에서 모듈 불러오기
mod2.py 파일을 mod3.py 파일에서 불러와 사용해 보자.
```
# coding: utf-8
import mod2

result = mod2.add( 3, 4 )
print( result )
```
`*.py` 파일이 동일한 디렉토리에 있어야 한다.  

sys, sys.path, sys.path.append 모듈을 사용하면 다른 디렉토리의 모듈을 사용할 수도 있다.