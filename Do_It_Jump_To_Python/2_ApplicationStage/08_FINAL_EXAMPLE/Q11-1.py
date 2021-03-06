# coding: utf-8
'''
## Q11 모듈 사용 방법
`/Users/Jeaha/doit` 디렉터리에 mymod.py 파이썬 모듈이 있다고 가정해 보자.  
명령 프롬프트 창에서 파이썬 셸을 열어 이 모듈을 import해서 사용할 수 있는 방법을 모두 기술하시오.  
(즉 다음과 같이 `import mymod`를 수행할 때 오류가 없어야 한다.)  
```
>>> import mymod
>>>
```

1) sys 모듈 사용하기
'''

import sys
sys.path.append("/Users/Jeaha/doit")
import mymod