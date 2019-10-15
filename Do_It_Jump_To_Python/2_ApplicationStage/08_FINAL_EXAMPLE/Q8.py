# coding: utf-8
'''
## Q8 역순 저장
다음과 같은 내용의 파일 abc.txt가 있다.
```
AAA
BBB
CCC
DDD
EEE
```
이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
```
EEE
DDD
CCC
BBB
AAA
```
파일 객체의 readlines를 사용하여 모든 라인을 읽은 후에 reversed를 사용하여 역순으로 정렬한 다음 다시 파일에 저장한다.
'''
f = open('/Users/Jeaha/git/Python_Study/Py/Application/08_EXAMPLE/Q8.txt', 'r')
lines = f.readlines()     # 모든 라인을 읽음
f.close()

lines.reverse()           # 읽은 라인을 역순으로 정렬

f = open('/Users/Jeaha/git/Python_Study/Py/Application/08_EXAMPLE/Q8.txt', 'w')
for line in lines:
  line = line.strip()     # 포함되어 있는 줄 바꿈 문자 제거
  f.write(line)
  f.write('\n')           # 줄 바꿈 문자 삽입

f.close()