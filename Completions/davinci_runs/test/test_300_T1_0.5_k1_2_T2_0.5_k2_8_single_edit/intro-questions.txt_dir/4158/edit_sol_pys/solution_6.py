# Accepted

n = int(input())
x = [int(i) for i in input().split()]
x.sort()

count = 1
curr = x[0]
for i in range(1, n):
    if x[i] - curr == 2:
        count += 1
        curr = x[i]
print(count)
print(curr, end=' ')
for i in range(1, n):
    if x[i] - curr == 2:
        print(x[i], end=' ')
        curr = x[i]
