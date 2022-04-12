
n = int(input())
a = [int(i) for i in input().split()]

for i in range(1, 5*10**8+2):
    for j in range(n):
        if a[j] == 2*i-1 or a[j] == 2*i:
            a[j] = 2*i-1 if a[j] == 2*i else 2*i

for i in range(n):
    print(a[i], end=' ')
