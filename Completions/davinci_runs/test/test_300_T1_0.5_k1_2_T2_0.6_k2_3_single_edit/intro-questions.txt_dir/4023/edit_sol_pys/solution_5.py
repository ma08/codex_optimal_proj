

n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n:  # n個中に同じ数字がある場合
    print("YES")
    exit()

a_sorted = sorted(a)  # 昇順ソート

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit()

print("YES")
