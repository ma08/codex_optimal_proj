import sys
import os


n = int(input())
s = input()

print(s[n:] + s[:n])
