

# cook your dish here
t = int(input())
while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    count = 0
    x = 0
    for i in range(n):
        if a[i] % k == 0:
            count += 1
        else:
            b.append(a[i] % k)
    b.sort()
    for i in range(n):
        if b[i] == 0:
            break
        x += b[i]
        if x % k == 0:
            count += 1
            break
    print(count)
    t -= 1
