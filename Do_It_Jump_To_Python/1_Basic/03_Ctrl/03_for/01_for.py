# coding: utf- 8
def title(titl):
  print('\n'+'>' * 10 + titl + '<' * 10)

title( ' 전형적인 for문 ' )

test_list = [1, 2, 3]
for i in test_list:
  print( i )

title( ' 다양한 for문 사용 ' )

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
  print(first + last)

title( ' for문의 응용 ' )
marks = [90, 25, 67, 45, 80]
no = 0
for mark in marks:
  no += 1
  if mark >= 60:
    print('%d번 합격.' % no )
  else:
    print('%d번 불합격.' % no )

title( ' for문의 continue ')
no = 0
for mark in marks:
  no += 1
  if mark < 60:
    continue
  print('%d번 합격!' % no )