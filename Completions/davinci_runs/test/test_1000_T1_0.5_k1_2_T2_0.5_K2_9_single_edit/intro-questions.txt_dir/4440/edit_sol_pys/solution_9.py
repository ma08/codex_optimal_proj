
import math

L = int(input())
a = 1
b = 1
c = 1
max_volume = 0

while a <= L:
    while b <= L:
        while c <= L:
            if a + b + c == L:
                volume = a * b * c
                if volume > max_volume:
                    max_volume = volume
            c += 1
        b += 1
    a += 1

print(max_volume)
