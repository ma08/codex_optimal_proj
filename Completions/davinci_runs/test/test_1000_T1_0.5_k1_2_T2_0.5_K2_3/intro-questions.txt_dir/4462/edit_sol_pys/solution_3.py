# 入力が10**5とかになったときに100ms程度早い
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))

# Other's answer
N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if a[i] % 2 == 0:
        continue
    elif a[i] % 4 == 0:
        continue
    else:
        print("No")
        exit()

print("Yes")
