
import math

num = int(input())

for i in range(num, 0, -1):
    for j in range(2, num):
        if math.pow(i, 1/j) % 1 == 0:
            print(int(i))
            exit()
