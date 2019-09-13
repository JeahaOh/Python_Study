# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title(' Key 리스트 만들기 ')
# 딕셔너리의 key만 모아서 리스트 객체를 반환한다.
a = {'name': 'JEJE', 'phone': '10204430', 'addr' : 'Berlin'}
print( a.keys() )

for k in a.keys():
  print( k )

print( list(a.keys())) 


title(' Value 리스트 만들기 values ')
'''
values 함수를 호출하면 dict_values 객체를 반환한다.
'''
print( a.values() )


title(' Key, Value 쌍 얻기 items ')
'''
items() 함수는 Key, Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 반환한다.
'''
print( a.items() )

title(' key:value 쌍 모두 지우기 clear ')
a.clear()
print( a )


title(' key로 value 얻기 get ')
a = {'name': 'JeaHa', 'phone': '43131020', 'addr' : 'Stavanger'}
print( a.get('name') )
print( a.get('phone') )


title(' 존재 하지 않는 키로 값 가져오기. ')
'''
a['없는 key']를 실행하면 오류를 발생시키고,
a.get('없는 key')를 실행하면 None을 리턴한다.

딕셔너리 안에 찾으려는 key가 없을 경우 미리 정해둔 디폴트 값을 지정해서 가져올 수도 있다.
a.get('없는 key', '디폴트 값')
'''
print( a.get(1) )
print( ( a.get(1, 'null')))
# print( a[1] )


title(' 해당 key가 딕셔너리 안에 있는지 조사하기 in ')
print( 'addr' in a)
print( 1 in a)