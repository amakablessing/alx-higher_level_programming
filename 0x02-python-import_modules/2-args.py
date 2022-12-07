#!/usr/bin/bash/python3
import sys

if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("0  arguments.")
    elif len(argv) == 1:
        print("1 argument:")
    else:
            print("{} argument {} 
