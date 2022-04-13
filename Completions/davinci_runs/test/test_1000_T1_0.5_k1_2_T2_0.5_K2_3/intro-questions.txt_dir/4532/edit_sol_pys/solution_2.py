

# cook your dish here
t = int(input())
while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    count = 0
    x = 0
    for i in range(n):
        if a[i]%k == 0:
            count += 1
        else:
            b[i] = k - (a[i]%k)
    b.sort()
    for i in range(n):
        x += b[i]
        if x%k == 0:
            count += 1
            break
    print(count)
    t -= 1
