#!/usr/bin/env python

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()

    if 'pop' == command[0]:
        s.pop()
    else:
        getattr(s, command[0])(int(command[1]))

print(sum(s))
