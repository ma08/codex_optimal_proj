

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(2)
else:
    count = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            count += 1
        else:
            break
    for j in range(n-2, 0, -1):
        if a[j] < a[j+1]:
            count += 1
        else:
            break
    print(count)