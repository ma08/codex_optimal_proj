
n = int(input())

for i in range(n):
    x = int(input())
    if i == 0:
        low = 1
        high = x
    else:
        low = x + 1
        high = x

for i in range(low, high + 1):
    print(i)
