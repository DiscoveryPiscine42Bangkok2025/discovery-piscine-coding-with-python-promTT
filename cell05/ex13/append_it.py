#!/usr/bin/env python
import sys
if len(sys.argv) == 1:
    print("none")
else:
    for i in range (1,len(sys.argv)):
        if "ism" in sys.argv[i]:
            continue
        else:
            print(sys.argv[i] + "ism")