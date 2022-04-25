# coding: utf-8
# Your code here!

k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
