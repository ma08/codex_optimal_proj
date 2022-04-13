

n = int(input())

for i in range(n):
    x = int(input())
    if i == 0:
        low = x
        high = x
    else:
        low = x + 1
        high = high * 2

for i in range(low, high+1):
    print(i, end=" ")
