# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' Q1 주어진 자연수가 홀수인지 짝수인지 판별하는 is_odd()를 만들자. ' )

def is_odd( n ):
  if n % 2 == 1:
    print( 'Odd' )
  else:
    print( 'Even' )

is_odd( input( "Enter No. : ") )

is_odd = lambda x: True if x % 2 == 1 else False
print( is_odd( input( "\nis odd\nEnter No. : ") ) )


title( ' Q2 입력으로 들어오는 모든 수의 평균을 계산해 주는 함수를 작성해 보자. ')
# def avg( *args ):
#   li = list(args)
#   sum = 0
#   for n in li:
#     sum += n
#   return sum / len(li)
def avg( *args ):
  result = 0
  for i in args:
    result += i
  return result / len( args )

print( avg(1, 2) )
print( avg(1, 2, 3, 4, 5) )
print( avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) )
# 소수점이 날아가네..?

title( ' Q3 3과 6을 입력했을 때 9가 아닌 36이라는 결과값을 돌려주었다. 이 프로그램의 오휴를 수정해 보자. ')
input1 = input('first No : ')
input2 = input('second No : ')

tot = input1 + input2
# 버전 업 되면서 문제의 의도가 흐려졌다.
# tot = int(input1) + int(input2)
print('Sum is %s.' % tot)


title( ' Q4 다음 중 출력 결과가 다른 것 한 개를 고르시오. ')
print( 'You' 'Need' 'python')
print( 'You' + 'Need' + 'python')
print( ('You', 'Need', 'python') )
print( "".join( ["You", "Need", "Python"] ) )

# 이전 버전은 콤마가 있는 경우 공백이 삽입되어 더해졌지만 지금은 튜플 형태로 출력이 된다..?

title( ' Q5 아래 프로그램은 우리가 예상한 "Life is too Short, You Need Python."라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자. ')
f1 = open( 'TEST.txt', 'w' )
f1.write( 'Life Is Too Short, You Need Python.' )
f1.close()  #

f2 = open( 'TEST.txt', 'r')
print( f2.read() )

title( ' Q6 사용자의 입력을 파일에 저장하는 프로그램을 작성해 보자.')
# cont = input("Enter Content :\n")
# f3 = open('TEST.txt', 'a')
# f3.write( cont )
# f3.write( '\n' )
# f3.close()

# 버전 문제일까? 
'''
Enter Content :
ASDF
Traceback (most recent call last):
  File "/Example.py", line 64, in <module>
    cont = input("Enter Content :\n")
  File "<string>", line 1, in <module>
NameError: name 'ASDF' is not defined
The terminal process terminated with exit code: 1
'''

title( ' Q7 다음과 같은 내용을 지닌 파일이 있다. 내용중 문자열을 바꾸어 저장해 보자. ')
f4 = open( 'JAVA.txt', 'r')
body = f4.read()
f4.close()

body = body.replace( 'Python', 'Java' )
f4 = open( 'JAVA.txt', 'w')
f4.write( body )
f4.close()
