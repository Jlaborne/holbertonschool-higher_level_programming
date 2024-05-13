#!/usr/bin/python3
def no_c(my_string):
    no_c_string = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            no_c_string += char
    return no_c_string
    
