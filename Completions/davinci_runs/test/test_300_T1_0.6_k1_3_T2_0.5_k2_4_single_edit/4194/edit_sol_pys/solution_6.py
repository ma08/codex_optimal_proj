
import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

days_for_assignment = sum(A)

if days_for_assignment > N:
    print(-1)
    sys.exit(0)

days_for_hanging_out = N - days_for_assignment

print(days_for_hanging_out)
