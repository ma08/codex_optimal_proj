
n = int(input())
a = list(map(int, input().split()))

if a.count(a[0]) == n or a.count(a[0]) == n - 1 and a[0] == 0:
    print("YES")
    exit()

a_sorted = sorted(a)

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit()

print("YES")
