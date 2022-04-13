

import math

V = int(input())
# округляем все вверх

a = math.ceil(V**(1/3))
b = math.ceil((V/a)**(1/2))
c = math.ceil(V/(a*b))

print(2*(a*b + b*c + a*c))
