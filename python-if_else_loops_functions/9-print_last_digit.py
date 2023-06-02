#!/usr/bin/python3
def print_last_digit(number):
    v_number = abs(number) % 10
    print("{}".format(v_number), end='')
    return v_number
