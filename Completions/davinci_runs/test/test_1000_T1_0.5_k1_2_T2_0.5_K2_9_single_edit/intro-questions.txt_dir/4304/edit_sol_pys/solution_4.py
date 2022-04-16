

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())  # 입력 받기

if a == 1:  # 예외 처리
    print(b - a)
else:
    print(b - a - 1)  # 나머지 처리
