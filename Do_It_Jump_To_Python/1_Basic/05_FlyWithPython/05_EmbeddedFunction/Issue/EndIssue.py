# coding: utf-8
from __future__ import print_function
'''
end=''
이슈
예제에서 end=''
코드가 실행 되지 않는 문제가 발생했음,
Mac에 Python 버전이 3.7.4로 설치했는데 2.7.10 버전으로 인식 되는 문제가 있고.
일단 2.7도 사용할 수도 있으니 end를 실행 하는 방법을 일단 알아보도록 함.

`https://stackoverflow.com/questions/2456148/python-print-end`

`from __future__ import print_function`
We need to import a header before using end=''.
as it is not included in the python's normal runtime

.py 파일의 상단에서 print function을 import 해준다.
'''
a = eval("raw_input()")
print( a, end= '..' )

