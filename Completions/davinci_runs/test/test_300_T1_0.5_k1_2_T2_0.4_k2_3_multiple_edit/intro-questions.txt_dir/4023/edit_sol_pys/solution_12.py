
n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n:
    print("YES")
    exit(0)

a_sorted = sorted(a)  # aを昇順に並び替えたリスト

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit(0)

print("YES")
