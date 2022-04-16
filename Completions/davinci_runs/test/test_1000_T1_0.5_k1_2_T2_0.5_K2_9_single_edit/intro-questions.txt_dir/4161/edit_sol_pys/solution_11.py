
import sys

K = int(sys.stdin.readline())
print(sum([gcd(gcd(a, b), c) for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1)]))
