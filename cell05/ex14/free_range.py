#!/usr/bin/env python
import sys
list = []
if len(sys.argv) != 3:
    print("none")
else:
    for i in range(int(sys.argv[1]),int(sys.argv[2])+1):
        list.append(i)
    print(list)