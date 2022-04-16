

k = int(input())

sum_ = []

for i in range(k):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = s
    for j in range(n):
        t -= a[j]
        if t in sum_:
            print("YES")
            print(sum_.index(t) + 1, j + 1)
            print(i + 1, j + 1)
            exit()
        sum_.append(t)

print("NO")
