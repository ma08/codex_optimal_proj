

import sys
import math

def distanceBetweenHands(hour, minute):
    hour = hour * 30.0
    minute = minute * 6.0

    x1 = 3.0 * math.cos(hour)
    y1 = 3.0 * math.sin(hour)
    x2 = 4.0 * math.cos(minute)
    y2 = 4.0 * math.sin(minute)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

params = sys.stdin.readline().split()
a = int(params[0])
b = int(params[1])
h = int(params[2])
m = int(params[3])

print(distanceBetweenHands(h, m))
