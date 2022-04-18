
import math

while True:
    num = input()
    num = num.split(' ')
    num = list(map(int, num))
    num.sort()
    num = num[1] - num[0]
    num = math.ceil(num / 10)
    print(num)
