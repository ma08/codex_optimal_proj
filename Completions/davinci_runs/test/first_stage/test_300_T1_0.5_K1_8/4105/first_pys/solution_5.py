

n, k = map(int, input().split())

if k == 1 or n == 2 or n == 3:
    print("NO")
else:
    print("YES")
    for i in range(1, n//2+1):
        print(i, k-i+1)
        print(k-i+1, i)
    if n % 2 == 1:
        print(n//2+1, k-n//2+1)