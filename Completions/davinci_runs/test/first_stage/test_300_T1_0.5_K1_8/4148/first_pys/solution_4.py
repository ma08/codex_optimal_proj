

import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

ans = ""

for s in S:
    ans += chr(ord(s)+N) if ord(s)+N <= ord('Z') else chr(ord(s)+N-26)

print(ans)