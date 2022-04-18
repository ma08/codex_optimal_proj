

# cook your dish here
t = int(input())
    x = 0
while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    count = 0
    for i in range(n):
        if a[i]%k == 0:
            count += 1
        else:
            b[i] = a[i]%k
    b.sort()
    for i in range(n):
        if b[i] == 0:
            break
        x += b[i]
        if x%k == 0:
            count += 1
            break
    print(count)
    t -= 1
