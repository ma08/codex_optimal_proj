
import sys

P, N = map(int, sys.stdin.readline().split())
parts = set()
for i in range(N):
    part = sys.stdin.readline().strip()
    if part not in parts:
        parts.add(part)
    if len(parts) == P:
        print(i + 1)
        break

else:
    print("paradox avoided")
