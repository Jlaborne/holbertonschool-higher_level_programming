#!/usr/bin/python3
import functools

def uniq_add(my_list=[]):
    return (functools.reduce(lambda a, b: a + b, set(my_list)))
