# coding: utf-8
'''
sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타낸다.
즉, 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있다.

'''
import sys
print( sys.path )
a = sys.path.append('/Users/Jeaha/git/Python_Study/PY/Python_Study/05_FlyWithPython/06_ExternalFunction/01_sys')
print( a )