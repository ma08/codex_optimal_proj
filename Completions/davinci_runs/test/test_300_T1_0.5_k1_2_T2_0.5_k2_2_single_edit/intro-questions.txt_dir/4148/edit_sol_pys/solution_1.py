# https://www.acmicpc.net/problem/5622

import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

ans = 0
for s in S: ans += min((ord(s) - ord('A')) // 3 + 3, 10)

print(ans)

# ord() : character to integer
# chr() : integer to character
