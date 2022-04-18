
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] != i + 1: # リストaのi番目の要素とi+1を比較
        ans += 1

print(ans)
