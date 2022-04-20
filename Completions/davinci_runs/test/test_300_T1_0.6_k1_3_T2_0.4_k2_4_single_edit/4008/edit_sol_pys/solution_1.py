
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

if len(set(a)) < k:
    print("NO")
else:
    print("YES")
    for i in range(n): print(i % k + 1, end=" ")
