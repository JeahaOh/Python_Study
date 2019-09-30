# coding: utf-8
'''
pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈.
pickle의 dump()을 이용하여 객체인 data를 그대로 파일에 저장해 보자.
'''
import pickle
f = open("pickle_test.txt", 'wb')
data = {1: 'Hell the', 2: 'Python'}
pickle.dump( data, f )
f.close()