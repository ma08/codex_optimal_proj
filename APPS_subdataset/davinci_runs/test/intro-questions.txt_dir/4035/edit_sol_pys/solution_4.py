
from math import floor

a, b = map(int, input().split())

for i in range(1, 101):
    if floor(i * 0.08) == a and floor(i * 0.1) == b:  # floor()は小数点以下切り捨て
        print(i)
        exit()

print(-1)
