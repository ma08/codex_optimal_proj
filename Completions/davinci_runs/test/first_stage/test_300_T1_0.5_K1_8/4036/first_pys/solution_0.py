

n, k = map(int, input().split())

if n > k or n < k - 1:
    print("NO")
elif n == k:
    print("YES")
    print(" ".join([str(1) for i in range(n)]))
else:
    print("YES")
    print(" ".join([str(i) for i in range(1, n-k+2)]))