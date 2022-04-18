import math

n = int(input())

num = int(math.sqrt(n))

if num * num == n:
    print(num)
else:
    print(num + 1)




