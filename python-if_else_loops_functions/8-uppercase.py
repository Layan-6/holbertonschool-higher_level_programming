#!/usr/bin/python3
def uppercase(str):
    for c in str:
        diff = 0
        if ord('a') <= ord(c) <= ord('z'):
            diff = 32
        print("{}".format(chr(ord(c) - diff)), end='')
    print()
