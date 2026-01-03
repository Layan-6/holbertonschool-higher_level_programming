#!/usr/bin/python3
result = ''
for i in range(97, 123):
    if i != 101 and i != 113:
        result += chr(i)
print("{}".format(result), end='' )
