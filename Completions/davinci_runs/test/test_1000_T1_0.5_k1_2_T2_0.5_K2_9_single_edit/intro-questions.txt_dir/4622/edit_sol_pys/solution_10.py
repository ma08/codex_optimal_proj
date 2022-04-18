import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

print("YES" if len(set(a)) == n else "NO")
