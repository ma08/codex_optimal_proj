import numpy as np

N = int(input())
H = list(map(int, input().split()))
H = np.array(H)
ans = 0
curr = 0
for i in range(N-1):
    if H[i] >= H[i+1]:
        curr += 1
    else:
        ans = max(ans, curr)
        curr = 0
print(max(ans, curr + 1))
