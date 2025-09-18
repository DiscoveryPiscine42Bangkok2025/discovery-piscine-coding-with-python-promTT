#!/usr/bin/env python
import sys
if len(sys.argv) != 3:
    print("none")
else:
    count = sys.argv[2].count(sys.argv[1])
    if count == 0:
        print("none")
    else:
        print(count)