# coding: utf-8
'''
명령 행에서 인수 전달하기 - sys.argv
terminal에서
`python 01_argv_test.py you need python`
처럼 파일명 뒤에 다른 값을 넣어주면 sys.argv가 리스트에 그 값이 추가된다.
'''
import sys
print( sys.argv )