import sys
input = sys.stdin.readline


N = int(input().rstrip())

count = 0
for i in range(1, N+1):
    count += len(str(i)) % 2

print(count)
