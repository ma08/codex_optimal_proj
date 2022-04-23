
import sys
import math

def distanceBetweenHands(hour, minute):
    hour *= 30.0
    minute *= 6.0

    x1 = 3.0 * math.cos(math.radians(hour))
    y1 = 3.0 * math.sin(math.radians(hour))
    x2 = 4.0 * math.cos(math.radians(minute))
    y2 = 4.0 * math.sin(math.radians(minute))

    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) 

params = sys.stdin.readline().split()
a = int(params[0])
b = int(params[1])
h = int(params[2])
m = int(params[3])

print(distanceBetweenHands(h, m))
