# coding: utf-8
'''
pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈.
pickle의 load()을 사용해서 원래 있던 객체 상태 그대로 불러온다
'''
import pickle
f = open("pickle_test.txt", 'rb')
data = pickle.load( f )
print( data )
f.close()