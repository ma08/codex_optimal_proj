

k = int(input())
n = int(input())

for i in range(n):
    time, zone = input().split()
    time = int(time)
    if (time + k) % 8 == 0:
        k = 8
    else:
        k = (time + k) % 8

print(k)
