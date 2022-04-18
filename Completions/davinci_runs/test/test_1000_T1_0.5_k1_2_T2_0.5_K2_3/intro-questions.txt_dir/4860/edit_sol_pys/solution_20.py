

n = int(input())

for i in range(n):
    x = int(input())
    if i == 0:
        low = 0
        high = x
    else:
        if low > x:
            low = x
        if high < x:
            high = x

for i in range(low, high+1):
    print(i)
