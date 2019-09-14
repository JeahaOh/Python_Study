# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

score = 80
if score >= 60:
  msg = 'pass'
else:
  msg = 'failure'

print( msg )

# Python의 conditional expression을 사용하면 다음과 같은 간단한 코드작성을 할 수 있다.
# 3항 연산?
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
msg = 'pass' if score >= 90 else 'failure'
print( msg )
