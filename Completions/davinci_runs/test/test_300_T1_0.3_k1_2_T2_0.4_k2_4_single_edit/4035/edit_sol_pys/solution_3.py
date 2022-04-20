

import sys

a, b = map(int, sys.stdin.readline().split())  # a, b를 입력받기

# a = 2
# b = 2

for i in range(1, 101):  # 1부터 100까지 반복하면서
    if int(i * 0.08) == a and int(i * 0.1) == b:
        print(i)
        exit()

print(-1)
