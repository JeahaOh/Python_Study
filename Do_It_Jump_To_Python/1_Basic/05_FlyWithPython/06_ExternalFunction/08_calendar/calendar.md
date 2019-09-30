# calendar

## calendar.calendar( 연도 )
그해의 전체 달력을 문자열로 반환.
```
>>> import calendar
>>> calen = calendar.calendar( 2019 )
>>> print( calen )

                                  2019
... 생략 ...
      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3                         1
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       2  3  4  5  6  7  8
14 15 16 17 18 19 20      11 12 13 14 15 16 17       9 10 11 12 13 14 15
21 22 23 24 25 26 27      18 19 20 21 22 23 24      16 17 18 19 20 21 22
28 29 30 31               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30 31
```

## calendar.prmonth( 년, 월 )
해당 년 월의 달력을 반환.
```
>>> calendar.prmonth( 2019, 12 )
   December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

## calendar.weekday( 년, 월, 일 )
날짜에 해당하는 요일을 리턴.
월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4, 토요일은 5, 일요일은 6
```
>>> calendar.weekday( 2019, 9, 17 )
1
```

## calendar.monthrange( 년, 월 )
입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 튜플로 리턴.
```
>>> calendar.monthrange( 2019, 9 )
(6, 30)
```
