#!/usr/bin/env python
list = [2, 8, 9, 48, 8, 22, -12, 2]
new_list = []
for i in list:
    i += 2
    new_list.append(i)
print(f"Original array: {list}")
print(f"New array: {new_list}")