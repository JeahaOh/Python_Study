# coding: utf-8
'''
## Q15 Duplicate Numbers
0~9의 문자로 된 숫자를 입력받았을 때,  
이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.  
```
입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: true false false true false
```

리스트 자료형을 사용하여 중복된 값이 있는지 먼저 조사한다.
중복된 값이 있을 경우는 False를 리턴한다.
최종적으로 중복된 값이 없을 경우 0~9까지의 숫자가 모두 사용되었는지 판단하기 위해
입력 문자열의 숫자 값을 저장한 리스트 자료형의 총 개수가 10인지를 조사하여
10일 경우는 True, 아닐 경우는 False를 리턴한다.
'''
def chkDupNum( s ):
  result = []
  for n in s:
    if n not in result:
      result.append( n )
    else:
      return False
  return len( result ) == 10

print(chkDupNum("0123456789"))      # True 리턴
print(chkDupNum("01234"))           # False 리턴
print(chkDupNum("01234567890"))     # False 리턴
print(chkDupNum("6789012345"))      # True 리턴
print(chkDupNum("012322456789"))    # False 리턴