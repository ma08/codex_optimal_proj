
import sys

A, B = map(int, input().split())
print(B // A + (B % A != 0)) # B // A: 몫 (정수), B % A: 나머지
