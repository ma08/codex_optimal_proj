

n = int(input())
a = list(map(int, input().split()))
a_sorted = sorted(a)
if a.count(a[0]) == n:
    print("YES")
    exit()


for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit()

print("YES")
