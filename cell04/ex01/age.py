#!/usr/bin/env python
age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
for i in range(1,4):
    print(f"In {i*10} years, you'll be {i*10+age} years old")