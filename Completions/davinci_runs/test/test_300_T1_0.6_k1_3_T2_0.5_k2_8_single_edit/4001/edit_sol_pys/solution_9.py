from functools import reduce


def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm


n = int(input())
divisors = list(map(int, input().split()))[:-1]

x = divisors.pop(0)
y = divisors.pop(0)

while divisors:
    x = lcm(x, divisors.pop(0))
    y = lcm(y, divisors.pop(0))

print(x, y)
