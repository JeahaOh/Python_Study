# 문자열의 인덱스와 잘라내기
ㅁ = 'Life is too short, You need Python.'
print(ㅁ)

print('ㅁ -7 : ' + ㅁ[-7])

# 문자열 슬라이싱.
b = ㅁ[0:4]
print('ㅁ[0:4] : ' + b)
'''
문자열 슬라이싱은
문자열[시작 idx : 끝 idx]으로, 끝 인덱스는 포함하지 않는다.
시작 idx <= 대상 문자열 < 끝 idx
'''

# 끝 idx를 생략하면 문자열의 끝까지 뽑아낸다.
print('ㅁ[19:] : ' + ㅁ[19:])

# 시작 idx를 생략하면 처음부터 끝까지 뽑아낸다.
print('ㅁ[:19] : ' + ㅁ[:19])

# 양쪽 idx 를 생랼하면 문자열의 처음부터 끝까지 뽑아낸다.
print('ㅁ[:] : ' + ㅁ[:])

# -idx 를 사용할 수 있다. 역시 ㅁ[-7]은 포함하지 않는다.
print('ㅁ[19:-7] : ' + ㅁ[19:-7])


print('=' * 20)
## 슬라이싱으로 문자열 나누기
a = '20190827Sunny'
date = a[:8]
weather = a[8:]
print('a : ' + a)
print('data : ' + date)
print('weather : ' + weather)

print('=' * 20)

year = a[:4]
date = a[4:8]
weather = a[8:]
print('a : ' + a)
print('year : ' + year)
print('data : ' + date)
print('weather : ' + weather)

print('=' * 20)
'''
Python의 String은 immutable한 자료형 이라고 함.
이는 문자열의 요솟값을 변경할 수 없기 때문임.
문자열의 요소를 바꾸려면 슬라이싱 기법을 사용해서 해야 함.
'''
a = 'pithon'
a = a[:1] + 'y' + a[2:]
print(a)