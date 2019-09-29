# coding: utf-8
'''
eval( expression )
실행 가능한 문자열을 인자로 받아 문자열을 실행한 결과 값을 돌려주는 함수.
입력 받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용.
'''
print( eval( ' 1 + 2 ' ) )
print( eval( '"Hell " + "the " + "Python."' ) )
print( eval( 'divmod( 4, 3)' ) )