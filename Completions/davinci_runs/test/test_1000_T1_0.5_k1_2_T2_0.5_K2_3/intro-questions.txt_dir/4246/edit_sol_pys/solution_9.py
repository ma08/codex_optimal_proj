import math


a, b, h, m = [int(x) for x in input().split()]

short = (a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(6 * m - 30 * h))) ** 0.5

for i in range(len(s)):
    if s[i] == t[i]:
        corrects += 1

print(corrects)
