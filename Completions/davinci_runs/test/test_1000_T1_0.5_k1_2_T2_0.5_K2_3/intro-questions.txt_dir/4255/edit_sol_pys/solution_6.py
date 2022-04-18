import math

abcd = input().split()
a, b, c, d = int(abcd[0]), int(abcd[1]), int(abcd[2]), int(abcd[3])

p = (a + b + c + d) / 2
print(math.sqrt(p * (p - a) * (p - b) * (p - c) * (p - d)))
