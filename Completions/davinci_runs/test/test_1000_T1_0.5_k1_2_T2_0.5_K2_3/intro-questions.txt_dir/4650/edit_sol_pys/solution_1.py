
# ----- Solution 1 -----
#!/usr/bin/python3
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for j in range(n):
        if a[j] % 3 == 0:
            count += 1
    for j in range(n):
        for k in range(j+1, n):
            if (a[j]+a[k]) % 3 == 0:
                count += 1
                break
    print(count)

# ----- Solution 2 -----
#!/usr/bin/python3
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for j in range(n):
        if a[j] % 3 == 0:
            count += 1
    for j in range(n):
        for k in range(j+1, n):
            if (a[j]+a[k]) % 3 == 0:
                count += 1
                break
    print(count)
