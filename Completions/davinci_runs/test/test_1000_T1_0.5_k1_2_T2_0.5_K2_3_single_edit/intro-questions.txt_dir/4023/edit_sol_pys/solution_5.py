
n = int(input(""))
a = list(map(int, input("").split()))

if a.count(a[0]) == n:
    print("YES", end="")
    exit()

a_sorted = sorted(a)

for i in range(n - 1):
    if a_sorted[i] + 1 != a_sorted[i + 1]:
        print("NO", end="")
        exit()

print("YES", end="")
