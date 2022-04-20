

from math import log10, ceil

N = int(input())

min_fb = ceil(log10(N))
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        min_fb = min(min_fb, ceil(log10(i)) + ceil(log10(N // i)))

print(min_fb)