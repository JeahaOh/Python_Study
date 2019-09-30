# random
random randint는 난수를 발생시키는 모듈이다.
```
import random
```
## random.random()
0.0에서 1.0사이의 실수 중에서 난수 값을 돌려준다.
```
>>> random.random()
0.24063730507897185
>>> random.random()
0.2799066555741513
>>> random.random()
0.9476808101060046
```

## random.randint( x, y )
x와 y 사이의 정수중에서 난수 값을 리턴.
```
>>> random.randint( 1, 45 )
22
>>> random.randint( 1, 45 )
13
>>> random.randint( 1, 45 )
38
>>> random.randint( 1, 45 )
41
>>> random.randint( 1, 45 )
35
>>> random.randint( 1, 45 )
30
>>> random.randint( 1, 45 )
38
```

