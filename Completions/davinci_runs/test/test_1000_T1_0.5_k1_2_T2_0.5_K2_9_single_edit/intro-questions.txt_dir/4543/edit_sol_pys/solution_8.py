
import math

a, b = map(int, input().split())  # a,b is an integer

num = int(str(a) + str(b))  # num is an integer

if math.sqrt(num).is_integer():  # if num is the square of an integer
    print("Yes")
else:
    print("No")
