# coding: utf-8
'''
주민등록 번호를 포함하고 있는 텍스트가 있다.
이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.

정규 표현식이 없다면 다음과 같은 순서로 프로그램을 작성 할 것이다.
1. 전체 텍스트를 공백 문자로 나눈다(split).
2. 나뉜 단어가 주민등록번호 형식인지 확인한다.
3. 단어가 주민등록번호 형식이라면 뒷자리를 * 로 변환한다.
4. 나뉜 단어를 다시 조합한다.
'''

data = '''
park 800905-1049118
kim 700905-2059118
'''

result = []
for line in data.split("\n"):
  word_result = []
  for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
      word = word[:6] + "-" + "*******"

    word_result.append(word)
  result.append(" ".join(word_result))

print("\n".join(result))
