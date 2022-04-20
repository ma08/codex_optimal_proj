
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    if a[i] > a[i-1]:
        print(a[i], end=" ")
    else:
        print(a[i-1], end=" ")
print(a[-1])
