#!/usr/bin/python3

def is_same_class(obj, a_class):
    return type(obj) is a_class

a = 1
if is_same_class(a, int):
    print(True)
if is_same_class(a, float):
    print(False)
if is_same_class(a, object):
    print(False)
