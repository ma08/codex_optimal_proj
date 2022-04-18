
import sys

n, p, q = map(int, sys.stdin.readline().rstrip().split())

print("paul" if (p + q) % (2 * n) < n else "opponent")
