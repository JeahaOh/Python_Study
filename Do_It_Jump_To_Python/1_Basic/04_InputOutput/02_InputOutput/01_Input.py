# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' Input의 사용 ' )
a = ''
a = input("Enter String : ")
print( a )

title( ' print ')

b = 123
print( b )

c = "Python"
print( c )

d = [1, 2, 3]
print( b )

# "로 둘러싸인 문자열은 + 연산과 동일하다.
print("Life" "is" "too short")
print("Life" + "is" + "too short")

# 문자열 띄어쓰기는 콤마로 한다?
print("Life", "is", "too short")

# 함 줄에 결과값 출력하기
for i in range(10):
  # print(i, end=' ')
  print( i )


# end= 가 먹히지 않는데 이유를 모르겠다.