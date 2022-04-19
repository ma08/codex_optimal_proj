

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    if a[i] > b[i]:
        a[i] = b[i]
    elif a[i] < b[i]:
        b[i] = a[i]
    else:
        a[i] = b[i] = 0

print(sum(a))
