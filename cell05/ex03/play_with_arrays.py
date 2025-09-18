#!/usr/bin/env python3
list = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()
for i in list:
    if i > 5:
        i += 2
        new_set.add(i)
print(list)
print(new_set)