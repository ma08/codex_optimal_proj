import math

n = int(input())

for i in range(n, 0, -1):
    if i == n:
        for j in range(2, n):
            if math.pow(i, 1 / j) % 1 == 0:
                print(int(i))
                exit()
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if math.pow(i, 1 / j) % 1 == 0:
                print(int(i))
                exit()
