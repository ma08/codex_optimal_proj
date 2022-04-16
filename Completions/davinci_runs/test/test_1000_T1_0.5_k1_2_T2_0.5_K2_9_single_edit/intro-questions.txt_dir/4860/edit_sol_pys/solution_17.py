

n = int(input())

for i in range(n):
    if i == 1:
        low = 1
        high = n
    else:
        low = n + 1
        high = n

for i in range(low, high+1):
    print(i)
