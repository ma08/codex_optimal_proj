

n, k = map(int, input().split())

if (n-k) >= 0:
    print("YES")
    for i in range(k):
        if (n-k) >= 0:
            print(1, end=" ")
            n -= 1
            k -= 1
        else:
            print(n, end=" ")
            n -= n
            k -= 1
else:
    print("NO")