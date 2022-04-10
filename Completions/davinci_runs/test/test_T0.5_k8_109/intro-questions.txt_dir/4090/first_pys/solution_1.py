

n = int(input())
a = input().split()

curr = -1
for i in range(n):
    if a[i] != a[i-1]:
        curr += 1

if curr == 0:
    print(len(a[0]))
else:
    print(len(a[0]) + curr - 1)