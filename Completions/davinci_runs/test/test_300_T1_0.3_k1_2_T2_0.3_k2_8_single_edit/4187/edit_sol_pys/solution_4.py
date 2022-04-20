
n = int(input())
a = list(map(int,input().split()))

max_rest = 0

for i in range(n):
    if a[i] == 0:
        max_rest += 1

for i in range(n):
    if a[i] == 1:
        max_rest += 1
    else:
        break

for i in range(n-1,-1,-1):
    if a[i] == 1:
        max_rest += 1
    else:
        break

print(max_rest)
