# time
```
import time
```
시간과 관련된 time 모듈이다.

## time.time()
UTC를 사용해서 현재 시간을 실수 형태로 반환한다.
```
>>> time.time()
1568710537.627753
```

## time.localtime()
`time.localtime()`은 `time.time()`이 반환한 값을 이용해 년월일시분초.. 의 형태로 반환해 주는 함수다.
```
>>> time.localtime( time.time() )
time.struct_time(tm_year=2019, tm_mon=9, tm_mday=17, tm_hour=17, tm_min=57, tm_sec=13, tm_wday=1, tm_yday=260, tm_isdst=0)
```

## time.asctime()
`time.asctime()`은 `time.localtime()`에 의해 반환된 튜플 형채의 값을 인수로 받아 날찌와 시간을 보기 쉬운 형태로 반환한다.
```
>>> time.asctime( time.localtime( time.time() ) )
'Tue Sep 17 18:00:06 2019'
```

## time.ctime()
`time.asctime( time.localtime( time.time() ) )`의 간단한 형식.  
현재 시간만 반환한다.
```
>>> time.ctime()
'Tue Sep 17 18:01:18 2019'
```

## time.strftime()
시간에 관계된 것을 세밀하게 표현하는 여러가지 포멧 코드를 제공.
- `%a` : 요일 줄임말
  - Tue
- `%A` : 요일
  - Tuesday
- `%d` : 달 줄임말
  - Sep
- `%D` : 달
  - September
- `%c` : 날짜와 시간을 출력
  - Tue Sep 17 22:00:57 2019
- `%d` : 날
  - 01 ~ 31
- `%H` : 24형식의 시간
  - 00 ~ 23
- `%h` : 12형식의 시간
  - 01 ~ 12
- `%j` : 1년 중 누적 날짜
  - 001 ~ 366
- `%m` : 달
  - 01 ~ 12
- `%M` : 분
  - 00 ~ 59
- `%p` : AM or PM
- `%S` : 초
  - 00 ~ 59
- `%U` : 1년 중 누적 주 일요일 기준
  - 00 ~ 53
- `%w` : 숫자로 된 요일 
  - 0 ~ 6
- `%W` : 1년 중 누적 주 원요일 기준
  - 00 ~ 53
- `%x` : 현재 설정된 로케일에 기반한 날짜 출력
  - 09/17/19
- `%X` : 현재 설정된 로케일에 기반한 시간 출력
  - 22:21:23
- `%Y` : 년도 출력
  - 2019
- `%Z` : 시간대 출력
  - KST
- `%y` : 2자리수 년도 출력
  - 19

```
>>> import time
>>> time.strftime('%c', time.localtime(time.time()))
'Tue Sep 17 22:24:18 2019'
```

## time.sleep( x )
루프 안에서 사용하면 일정시간 간격으로 루프를 실행.
x는 초 단위이다.
```
import time
>>> for i in range( 10 ):
...     print( i )
...     time.sleep( 1 )
... 
0
1
2
3
4
5
6
7
8
9
```