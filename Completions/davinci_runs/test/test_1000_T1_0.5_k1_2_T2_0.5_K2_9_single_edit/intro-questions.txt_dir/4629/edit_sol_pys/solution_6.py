

t = int(input())

for i in range(t):
    n = int(input())
    power = 0
    while 3**power < n:
        power += 1
    print(3**power)
