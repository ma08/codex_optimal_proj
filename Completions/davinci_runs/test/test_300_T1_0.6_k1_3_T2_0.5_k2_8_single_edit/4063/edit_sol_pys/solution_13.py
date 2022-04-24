import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

# print(n)
# print(a)

count = 0
for i in range(1, n):
    if sum(a[:i]) == sum(a[i:]):
        count += 1

print(count)
