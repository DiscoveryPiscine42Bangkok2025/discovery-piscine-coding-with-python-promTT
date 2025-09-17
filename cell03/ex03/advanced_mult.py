#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        result = f"Table de {i}:"
        j = 0
        while j <= 10:
            result += f" {i*j}"
            j += 1
        print(result)
        i += 1