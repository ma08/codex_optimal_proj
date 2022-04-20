

#Solution
import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
 
if k > n - 2:
    k = n - 2
 
a = []
 
for i in range(n - 1):
    a.append(int(input()))
 
print(k + 1)
 
for i in range(n - 1):
    print(i % (k + 1) + 1, end=' ')