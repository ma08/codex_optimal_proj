
import sys
# sys.stdin = open('in.txt', 'r')
# sys.stdout = open('out.txt', 'w')

n = int(input())
a = list(map(int, input().split()))

a.sort()

# print(a)

s = 0
for i in range(n):
    s += a[i]*(i+1) + 1

print(s)
print(*[i+1 for i in range(n)])
