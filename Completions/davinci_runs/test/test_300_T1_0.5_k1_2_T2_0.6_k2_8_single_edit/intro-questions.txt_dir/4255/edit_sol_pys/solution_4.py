

import math

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

print(math.sqrt(p * (p - a) * (p - b) * (p - c))
      for p in (a + b + c) / 2 if a >= b and a >= c and b >= c or
                a >= b and a >= c and c >= b or
                b >= a and b >= c and a >= c or
                b >= a and b >= c and c >= a or
                c >= a and c >= b and a >= b or
                c >= a and c >= b and b >= a)
