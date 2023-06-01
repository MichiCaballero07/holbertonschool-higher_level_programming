#!/usr/bin/python3
for num in range(10):
    for nu in range(num + 1, 10):
        if num == 8 and nu == 9:
            print("{}{}".format(num, nu), end="\n")
        else:
            print("{}{}".format(num, nu), end=", ")