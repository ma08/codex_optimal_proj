
import math
import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))[:N]

days_for_assignments = math.ceil(sum(A))

if days_for_assignments > N:
    print(-1)
    sys.exit(0)

days_for_hanging_out = N - days_for_assignments

print(days_for_hanging_out)
