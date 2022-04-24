# -*- coding: utf-8 -*-

n = int(input())
words = [input() for i in range(n)]

for i in range(1,n):
    if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
        print("No")
        exit()

print("Yes")
