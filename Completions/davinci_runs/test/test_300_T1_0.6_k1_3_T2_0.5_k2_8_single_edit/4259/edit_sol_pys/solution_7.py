

import sys, re

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

ans = 0
for i in range(N):
    if re.match(r"^(dream|dreamer|erase|eraser)+$", S[i:]):
        ans += 1
        break

if ans == 0:
    print("NO")
else: 
    print("YES")
