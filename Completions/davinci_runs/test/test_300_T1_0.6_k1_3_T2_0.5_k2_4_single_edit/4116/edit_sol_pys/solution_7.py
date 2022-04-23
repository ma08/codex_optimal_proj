
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(n - 1):
    if a[i] == a[i + 1]:
        print('NO')
        exit()
print('YES')
