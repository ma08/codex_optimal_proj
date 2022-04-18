N = int(input())
a = [int(input()) for i in range(N)]
 
ans = 0
for i in range(N):
    while a[i] % 2 == 0:
        a[i] //= 2
        ans += 1
 
print(ans)

K, X = map(int, input().split())

for i in range(X - K + 1, X + K):
    print(i, end=' ')
