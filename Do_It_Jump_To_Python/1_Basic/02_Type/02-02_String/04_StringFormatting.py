# 1. 숫자 바로 대입
temp = 'I eat %d apples'
print(temp % 3)

# 2. 문자열 바로 대입
temp = 'I eat %s apples'
print(temp % 'five')

# 3. 숫자 변수 대입
n = 7
temp = 'I eat %d apples'
print(temp %n)

# 4. 2개 이상의 값 넣기
n = 10
d = 'three'
temp = 'I ate %d apples. So I was sick for %s days.'
print(temp % (n, d))

'''
문자열 포멧 코드
%s  : 문자열 String
%c  : 문자 1개 Character
%d  : 정수 Integer
%f  : 부동 소수 Floating-point
%o  : 8진수
%x  : 16진수
%%  : Literal % (문자 '%' 자체)

## %s 를 사용할 경우 어떤 타입이던지 문자열로 변환해서 넣음.
'''
n = 3
r = 3.346
temp = 'I have %s albums, rate is over %s.'
print(temp %(n, r))


# 포메팅 연산자 %d와 %를 같이 쓸 경우
print('Error is %d%%.' %98)

