
import sys
N = int(sys.stdin.readline())

ans = 0
while N > 0:
    if N % 2 == 0:
        N = N // 2
    else:
        N -= 1
    ans += 1

print(ans)
