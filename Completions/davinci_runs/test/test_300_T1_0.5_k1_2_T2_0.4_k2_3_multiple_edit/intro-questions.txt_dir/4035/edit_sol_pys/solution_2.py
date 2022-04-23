

import math  # import the math module

a, b = map(int, input().split())  # a, b = map(int, input().split())

for i in range(1, a+1):  # for i in range(1, a+1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:  # if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(i)  # print(i)
        exit()  # exit()
print(-1)  # print(-1)
