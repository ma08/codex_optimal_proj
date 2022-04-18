

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())  # 공백 기준으로 구분하여 입력 받기
print(B // A + (B % A != 0))  # 몫 + 나머지가 있으면 1 추가
