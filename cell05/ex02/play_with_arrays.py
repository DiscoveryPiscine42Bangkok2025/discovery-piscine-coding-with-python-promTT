#!/usr/bin/env python
list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []
for i in list:
    if i > 5:
        i += 2
        new_list.append(i)
print(list)
print(new_list)