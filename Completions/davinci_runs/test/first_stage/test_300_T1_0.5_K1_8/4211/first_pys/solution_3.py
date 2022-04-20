

"""
n = int(input())
b = list(map(int, input().split()))

c = [0]*n
c[0] = 0
c[1] = b[0]

for i in range(2, n):
    c[i] = max(c[i-1], c[i-2]+b[i-1])

print(c[-1])
"""

n = int(input())
b = list(map(int, input().split()))

a = [0]*n
a[0] = 0
a[1] = b[0]

for i in range(2, n):
    a[i] = max(a[i-1], a[i-2]+b[i-1])

print(a[-1])