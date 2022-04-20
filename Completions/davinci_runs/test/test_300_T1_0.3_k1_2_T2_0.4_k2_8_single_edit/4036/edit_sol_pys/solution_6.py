

n, k = map(int, input().split())

if n < k or n > k*2:
    print("NO")
else:
    print("YES")
    for i in range(k):
        if n > 2*i+1:
            print(i+1, end=" ")
            n -= i+1
        else:
            print(n, end=" ")

            n = 0
