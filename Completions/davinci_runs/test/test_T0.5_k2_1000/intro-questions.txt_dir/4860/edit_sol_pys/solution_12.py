
low = 0
high = 0
n = int(input())

for i in range(n):
    x = int(input())
    if x < low:
        low = x
    if x > high:
        high = x

for i in range(low, high+1):
    print(i)
