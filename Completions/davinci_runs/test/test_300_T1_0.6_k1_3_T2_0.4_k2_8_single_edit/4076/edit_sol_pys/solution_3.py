
import sys
import math

def distanceBetweenHands(hour, minute):
    hour = hour * 30.0
    minute = minute * 6.0

    x1 = a * math.cos(math.radians(hour))
    y1 = a * math.sin(math.radians(hour))
    x2 = b * math.cos(math.radians(minute))
    y2 = b * math.sin(math.radians(minute))

    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

params = sys.stdin.readline().split()
a = int(params[0])
b = int(params[1])
h = int(params[2])
m = int(params[3])

print(distanceBetweenHands(h, m))
