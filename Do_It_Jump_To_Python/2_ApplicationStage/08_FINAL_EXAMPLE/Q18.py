# coding: utf-8
'''
## Q18 문자열 검색
다음 코드의 결괏값은 무엇일까?  
```
>>> import re
>>> p = re.compile("[a-z]+")
>>> m = p.search("5 python")
>>> m.start() + m.end()
```

정규식 `[a-z]+`은 소문자로 이루어진 단어를 뜻하므로 `5 python` 문자열에서 `python`과 매치될 것이다.
따라서 `python` 문자열의 시작 인덱스( `m.start()` )는 2이고 마지막 인덱스( `m.end()` )는 8이므로 10이 출력된다.
'''

import re

p = re.compile( '[a-z]+' )
m = p.search( '5 python' )

print( m.start() + m.end() )