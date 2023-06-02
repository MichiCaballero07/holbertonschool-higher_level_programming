#!/usr/bin/python3
import sys
n_args = len(sys.argv) - 1
if __name__ == "__main__":
    if n_args == 0:
        print('{} arguments.'.format(n_args), end="\n")
    elif n_args == 1:
        print('{} argument:'.format(n_args), end="\n")
        print('{}: {}'.format(n_args, sys.argv[1]), end="\n")
    else:
        print('{} arguments:'.format(n_args))
        for i in range(n_args):
            print('{}: {}'.format(i + 1, sys.argv[i + 1], end="\n"))
