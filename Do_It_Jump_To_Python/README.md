# Python_Study
Python을 공부해 보자.
**Do it!** `Jump to Python`  

## 실행 환경
- VS Code latest
  - Extension : Python (ver 2019.8.30787)
- Win 10
  - Python 3.7.4
  - Intel i7 CPU 2.20GHz
  - 16GB RAM
- MacOS Mohave 10.14.6
  - Python 2.7.0
  - Intel i7 CPU 2.6GHz
  - 36GB RAM

## 30일 진도 표
01. 01장
02. 02-1 ~ 02-2
03. 02-3 ~ 02-4
04. 02-5 ~ 02-6
05. 02-7
06. 02-8
07. 02장 연습문제
08. 03-1
09. 03-2
10. 03-3
11. 03장 연습문제
12. 04-1
13. 04-2
14. 04-3
15. 04장 연습문제
16. 05-1
17. 05-2
18. 05-3
19. 05-4
20. 05-5
21. 05-6
22. 05장 연습문제
23. 복습
24. 06-1 ~ 06-3
25. 06-4 ~ 06-6
26. 07-1
27. 07-2
28. 07-3
29. 복습
30. 시험

## 16회 진도표
01. 01장
02. 02장 자료형 - 1
03. 02장 자료형 - 2
04. 03장 제어문 - 1
05. 03장 제어문 - 2
06. 04장 입출력 - 1
07. 04장 입출력 - 2
08. 복습
09. 05장 클래스, 모듈
10. 05장 패키지, 예외처리
11. 05장 내장함수, 회장함수
12. 06장 1, 2, 3
13. 06장 4, 5, 6
14. 정규표현식 - 1
15. 정규표현식 - 2
16. 시험

## 2019.08.28
Window에서 작성한 코드가 Mac에서 작동하지 않는 문제 발견.  
```
File "/Users/Jeaha/git/Python_Study/Do_It_Jump_To_Python/1_Basic/01_Python/01-05_Python/05_function.py", line 1
SyntaxError: Non-ASCII character '\xed' in file /Users/Jeaha/git/Python_Study/Do_It_Jump_To_Python/1_Basic/01_Python/01-05_Python/05_function.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
The terminal process terminated with exit code: 1
```
encoding 문제.  
*.py 파일 1번줄에 다음 두개의 주석중 하나만 넣어주면 utf-8로 작동함.
```
# - *- coding: utf- 8 - *-
# coding: utf- 8
```
