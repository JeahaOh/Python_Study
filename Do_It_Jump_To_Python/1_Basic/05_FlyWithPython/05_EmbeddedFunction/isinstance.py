# coding: utf-8
'''
isinstance( object, class )
첫 번째 인수로 오는 obj가
두 번째 인수의 클래스인지 아닌지 반환
'''
class TEST: pass

t = TEST()
i = 3
print( isinstance(t, TEST) )
print( isinstance(i, TEST) )