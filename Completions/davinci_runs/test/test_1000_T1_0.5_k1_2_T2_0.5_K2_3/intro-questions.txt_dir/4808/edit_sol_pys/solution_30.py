

# n, dm = map(int, input().split())
# d_list = list(map(int, input().split())) # d_list is a list of days

# k = 0
# while k < n and d_list[k] > dm:
#     k += 1

# if k == 0:
#     print("It had never snowed this early!")
# else:
#     print("It hadn't snowed this early in {} years!".format(k))

import math

def f(a,b,c,d):
    return b*math.pow(a,c)-d

a = 0
b = 0
c = 0
d = 0

a,b,c,d = map(int, input().split())

print(f(a,b,c,d))
