

import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 30min

N = int(readline())
A = list(map(int, readline().split()))


def check(A):
    B = A[:]
    for i in range(1, N):
        if B[i - 1] > B[i]:
            B[i] = B[i - 1]
        elif B[i - 1] == B[i]:
            continue
        elif B[i - 1] + 1 < B[i]:
            return False

    return True


ans = "Yes"
for i in range(N):
    if check(A[:i] + A[i + 1:]):
        continue
    else:
        ans = "No"
        break

print(ans)
