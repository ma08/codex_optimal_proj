
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
print("YES")
for i in range(k):
    print(a[i], end=" ")
