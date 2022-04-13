

n = int(input())

for i in range(n):
    x = int(input())
    if i == 0:
        low = 0
        high = x
    else:
        if x > high:
            high = x
        elif x < low:
            low = x

for i in range(low, high+1):
    print(i)
