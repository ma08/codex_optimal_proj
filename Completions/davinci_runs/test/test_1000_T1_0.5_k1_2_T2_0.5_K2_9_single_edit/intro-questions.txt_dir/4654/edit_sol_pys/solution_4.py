

# Code 

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if (n % 2) != (k % 2):
        print("NO")
    else:
        if k == 1:
            print("YES")
            print(n)
        else:
            if n % 2 == 0:
                if n % k == 0:
                    print("YES")
                    for j in range(k):
                        print(n // k, end=' ')
                    print()
                else:
                    print("NO")
            else:
                if n % k == 1:
                    print("YES")
                    for j in range(k - 1):
                        print(n // k, end=' ')
                    print(n // k + 1)
                else:
                    print("NO")
