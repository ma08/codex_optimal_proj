
from math import sqrt

ab, bc = map(int, input().split())
hypotenuse = sqrt(ab ** 2 + bc ** 2)
print(int(hypotenuse * 2))
