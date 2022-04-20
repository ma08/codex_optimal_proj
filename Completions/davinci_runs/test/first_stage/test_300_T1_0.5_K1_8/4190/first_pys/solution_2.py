

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0]*n

for i in range(n):
    c[(a[i]+b[i])%n] += 1

if c[0] > 1:
    print("-1")
else:
    for i in range(n):
        if c[i] == 0:
            print("-1")
            break
    else:
        for i in range(n):
            print(c[i], end=" ")
        print()