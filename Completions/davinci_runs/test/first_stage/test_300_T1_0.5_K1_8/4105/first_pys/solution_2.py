

n, k = map(int, input().split())

if n == 2:
    print("YES")
    print("1", "2")
    print("2", "1")
elif n % 2 == 0:
    print("YES")
    for i in range(1, n//2 + 1):
        print(i, (i+1)%k+1)
        print((i+1)%k+1, i)
else:
    print("NO")