

import sys
input = sys.stdin.readline

n = int(input())  # n 개의 수
l = list(map(int, input().split()))  # n 개의 수가 공백으로 구분되어 입력됨

if max(l) < sum(l) - max(l):
    print("Yes")
else:
    print("No")
