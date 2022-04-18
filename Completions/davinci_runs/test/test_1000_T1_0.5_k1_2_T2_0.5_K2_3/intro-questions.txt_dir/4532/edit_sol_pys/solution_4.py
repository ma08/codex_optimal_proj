

# cook your dish here 
t = int(input())
while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    x = 0
    for i in range(n):
        if a[i]%k == 0:
            count += 1
        else:
            x += a[i]%k
            if x%k == 0:
                count += 1
                x = 0
    print(count)
    t -= 1
