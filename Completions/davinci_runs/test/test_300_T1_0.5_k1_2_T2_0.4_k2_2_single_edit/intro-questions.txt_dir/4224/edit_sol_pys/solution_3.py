import sys
import math


def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))

    # solve
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            ans += 1

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1

print(ans)
