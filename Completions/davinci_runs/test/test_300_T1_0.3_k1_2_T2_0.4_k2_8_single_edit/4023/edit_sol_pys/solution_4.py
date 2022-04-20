

n = int(input())
a = list(map(int, input().split()))
print('YES' if a[0] == a[n-1] and all(a[i-1] == a[i] for i in range(1, n)) else 'NO')
