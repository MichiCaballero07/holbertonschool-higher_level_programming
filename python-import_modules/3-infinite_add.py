#!/usr/bin/python3
import sys
args = sys.argv[1:]
if __name__ == "__main__":
    result = sum(int(arg) for arg in args)
    print("{}".format(result))
