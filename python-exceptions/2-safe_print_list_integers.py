#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for item in my_list:
            if printed_count < x:
                try:
                    print("{:d}".format(item), end='')
                    printed_count += 1
                except ValueError:
                    pass
        print()
        if x > len(my_list):
            raise IndexError("x is greater than the length of my_list")
    except TypeError:
        pass
    return printed_count
