# coding: utf-8
'''
input( [prompt] )
이슈
https://stackoverflow.com/questions/21122540/input-error-nameerror-name-is-not-defined

'''

"""
input function in Python 2.7,
evaluates whatever your enter, as a Python expression.
If you simply want to read strings,
then use raw_input function in Python 2.7, which will not evaluate the read strings.
"""
a = eval("raw_input()")
print( a )

