
import math
num = int(input())

for i in range(num, 1, -1):
    if i == num:
        for j in range(2, num):
            if math.pow(i, 1/j) % 1 == 0:
                print(int(i))
                exit()
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if math.pow(i, 1/j) % 1 == 0:
                print(int(i))
                exit()
