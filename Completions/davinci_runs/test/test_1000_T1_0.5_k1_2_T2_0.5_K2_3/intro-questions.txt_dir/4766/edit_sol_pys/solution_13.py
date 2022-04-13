#!/usr/bin/env python

# Simon says: print the second line if the first line starts with "Simon says"

for _ in range(int(input())):
    if input().startswith("Simon says"):
        print(input())
