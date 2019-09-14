# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' Q1 ' )
a = 'Life is too short, you need python'

if 'wife' in a: print( 'wife' )
elif 'phthon' in a and 'you' not in a: print( 'python' )
elif 'shirt' not in a: print( 'shirt' )
elif 'need' in a: print( 'need' )
else: print('none')

title( ' Q2 ')
n = 1
sum = 0
while n <= 1000:
  if n % 3 == 0:
    sum += n
  n+=1

print( sum )

title( ' Q3 별 찍기 ')
x = 1
while x <= 5:
  print( '*' * x )
  x += 1

title( ' Q4 1 ~ 100 ')
for i in range( 1, 101 ):
  print(i)

title( ' Q5 ')
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
avg = 0
for n in a:
  avg += n

print( avg / len(a) )

title( ' Q6 ')
ns = [1, 2, 3, 4, 5]
result = []
for n in ns:
  if n % 2 == 1:
    result.append(n * 2)
print( result )

rs = [ n * 2 for n in ns if n % 2 == 1 ]
print( rs )