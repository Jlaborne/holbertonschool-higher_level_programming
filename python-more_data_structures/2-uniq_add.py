#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_num = set(my_list)
    total = 0
    for num in unique_num:
        total += num
    return (total)
