

n, k = map(int, input().split())

if n%2 != 0:
    print("NO")
elif k == 1:
    print("YES")
    for i in range(n//2):
        print(1, 1)
else:
    print("YES")
    for i in range(n//2):
        print(i%k+1, k)