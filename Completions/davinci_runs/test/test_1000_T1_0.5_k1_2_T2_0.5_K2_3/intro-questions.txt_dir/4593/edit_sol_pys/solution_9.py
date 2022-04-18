
import math

n = int(input())

for i in range(n, 1, -1)
    for j in range(2, int(math.sqrt(i)) + 1)
        if math.pow(i, 1 / j) % 1 == 0
            print(int(i))
            exit()
