
import sys
input = sys.stdin.readline

n = int(input().rstrip())
t, a = map(int, input().rstrip().split())
h = list(map(int, input().rstrip().split()))

index = 0
diff = 10000

for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < diff:
        diff = abs(a - (t - h[i] * 0.006))
        index = i + 1

print(index)
