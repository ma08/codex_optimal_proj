n, k = map(int, input().split())

if n % k == 0:
    print("YES")
    for i in range(k):
        print(n // k, end=" ")
else:
    print("NO")
