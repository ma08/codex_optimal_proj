

n = int(input())
a = list(map(int, input().split()))

a.sort()

for i in range(1, n):
    if a[i] == a[i - 1]:
        print('NO')
        exit()

print('YES')
