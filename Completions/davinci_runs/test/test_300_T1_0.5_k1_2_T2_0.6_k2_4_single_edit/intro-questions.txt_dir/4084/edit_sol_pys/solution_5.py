

n = int(input())

a = [int(input()) for i in range(n)]

b = [int(input()) for i in range(n)]

c = [int(input()) for i in range(n)]

count = 0

for i in range(n):
    if i == 0:
        if a[i] == b[i] == c[i]:
            count += 1

    elif i == n - 1:
        if a[i] == b[i] == c[i]:
            count += 1

    else:
        if a[i] == b[i] == c[i]:
            count += 1
        elif a[i] == b[i]:
            count += 1
        elif b[i] == c[i]:
            count += 1
        elif a[i] == c[i]:
            count += 1

print(count)
