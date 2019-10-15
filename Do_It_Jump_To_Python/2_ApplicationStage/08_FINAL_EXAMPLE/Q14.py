# coding: utf-8
'''
## Q14 문자열 압축하기
문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.  
  
```
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
```

먼저 입력 문자의 문자를 확인하여 동일한 문자가 들어올 경우에는 해당 문자의 숫자값을 증가시킨다.
만약 다른 문자가 들어올 경우에는 해당 문자의 숫자 값을 1로 초기화 하는 방법을 사용하여 작성
'''
def comp_str(s):
  _c = ''
  cnt = 0
  result = ''

  for c in s:
    if c != _c:
      _c = c
      if cnt: result += str( cnt )
      result += c
      cnt = 1
    else:
      cnt += 1

  if cnt: result += str(cnt)  
  return result

print( comp_str( 'aaabbcccccca' ) )