#!/usr/bin/python3

name = input().strip()
new_name = name[0]

for i in range(1, len(name)):
    if name[i] != name[i-1]:
        new_name += name[i]

print(new_name)
