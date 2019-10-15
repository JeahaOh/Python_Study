# coding: utf-8
'''
다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.  
sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을  
result.txt 파일에 쓰는 프로그램을 작성하시오.  
```
70
60
55
75
95
90
80
80
85
100
```
'''
f = open('/Users/Jeaha/git/Python_Study/Py/Application/08_EXAMPLE/Q9.txt')
lines = f.readlines()   # Q9.txt를 줄단위로 모두 읽는다.
f.close()

total = 0
for line in lines:
  score = int( line )   # 줄에 적힌 점수를 숫자형으로 변환한다.
  total += score

avg = total / len( lines )

print( avg )

f = open('/Users/Jeaha/git/Python_Study/Py/Application/08_EXAMPLE/Q9_result.txt', 'w')
f.write( str( avg ) )
f.close()
'''
Q9.txt의 점수를 모두 읽기 위해 파일을 열고 readlines를 사용하여 각 줄의 점수 값을 모두 읽어 들여 총 점수를 구한다.
총 점수를 Q9_result.txt 파일의 라인(Line) 수로 평균 값을 구한 후
result.txt 파일에 바로 쓸 수 없으므로 str함수를 사용하여 문자열로 변경한 후
그 결과를 result.txt에 쓴다.
'''
