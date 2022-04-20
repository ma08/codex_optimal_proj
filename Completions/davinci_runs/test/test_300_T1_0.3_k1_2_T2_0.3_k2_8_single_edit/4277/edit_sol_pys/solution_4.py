
import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split()) # 공백으로 구분하여 입력받기

if n * a <= b:
    print(n * a)
else:
    print(b)
