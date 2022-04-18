import sys
from collections import Counter

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

c = Counter(S)

ans = 0
for i in range(N-2):
    if S[i:i+3] == "ABC":
        ans += 1

print(ans)
