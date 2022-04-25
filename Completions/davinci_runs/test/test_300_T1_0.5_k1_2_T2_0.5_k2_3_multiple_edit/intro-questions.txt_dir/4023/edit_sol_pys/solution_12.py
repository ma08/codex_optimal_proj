
n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a)

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO")
        exit()

print("YES")
