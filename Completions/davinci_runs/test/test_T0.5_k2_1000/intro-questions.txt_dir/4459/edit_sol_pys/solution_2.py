
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] != i + 1:  # i + 1 と i番目の要素が等しくない場合
        ans += 1

print(ans)
