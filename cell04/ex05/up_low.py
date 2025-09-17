#!/usr/bin/env python
inp = input()
result = ""
for i in inp:
    if "A" <= i <= "Z":
        result += i.lower()
    elif "a" <= i <= "z":
        result += i.upper()
    else:
        result += i
print(result)