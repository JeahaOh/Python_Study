# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

'''
변수의 선언
다른 언어처럼 = (assignment) 기호를 사용한다.
Python은 변수에 저장된 값을 스스로 판단해서 자료형을 저장하기 때문에 따로 선언할 필요가 없다.
'''
a = 1
b = 'python'
c = [1, 2, 3]

'''
변수?
Python에서 사용하는 변수는 객체를 가리티는 것이라고 말할 수 있음.
a = [1, 2, 3]으로 선언하면
[1, 2, 3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에 생성되고,
변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가리키게 됨.
'''
a = [1, 2, 3]
# 변수가 가리키는 메모리의 주소는 다음과 같이 확인할 수 있다.
print( id(a) )