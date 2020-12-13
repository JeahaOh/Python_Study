# 기본 데이터 타입

Python에서 사용 되는 기본 데이터 타입(Scalar Data Type)은 다음과 같다.

| type  |         desc         |       ex        |
| :---: | :------------------: | :-------------: |
|  int  |    정수형 데이터     | 100, 0xFF, 0o56 |
| float | 소숫점을 포함한 실수 |      10.25      |
| bool  |       참/거짓        |   True, False   |
| None  |  Null 과 같은 표현   |      None       |

정수형은 소숫점을 갖지 않는 정수.  
float은 소숫점을 갖는 데이터.  
bool은 boolean.  
None은 아무 데이터도 갖지 않는 표현으로 Null, Undefiened와 같다.  
정수형에 0x는 16진수 0o는 8진수를 의미하며 대소문자를 구분하지 않음.

리터럴 데이터를 특정 타입으로 변경하기 위해 int(), float(), bool()과 같은 타입 생성자를 사용 할 수 있음.

- 01_Type.py
  - ```python
      int(3.5)  # 3
      2e3       # 2000.0
      float('1.5')
    ```
