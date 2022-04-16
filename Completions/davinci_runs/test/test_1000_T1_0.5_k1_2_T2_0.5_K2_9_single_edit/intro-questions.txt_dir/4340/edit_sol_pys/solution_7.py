
n = int(input())
a = [int(i) for i in input().split()]

for i in range(1, 5 * 10 ** 8 + 1):
    for j in range(n):
        if a[j] == 2 * i - 1:
            a[j] = 2 * i
        elif a[j] == 2 * i:
            a[j] = 2 * i - 1

for i in range(n):
    print(a[i], end=' ')
