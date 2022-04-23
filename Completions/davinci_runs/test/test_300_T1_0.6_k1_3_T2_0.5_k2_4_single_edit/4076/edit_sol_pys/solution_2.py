
import sys
import math

def distanceBetweenHands(hour, minute):
    hour *= 5.0
    minute *= 6.0

    x1 = 3.0 * math.cos(math.radians(hour + minute / 12.0))
    y1 = 3.0 * math.sin(math.radians(hour + minute / 12.0))
    x2 = 4.0 * math.cos(math.radians(minute)) 
    y2 = 4.0 * math.sin(math.radians(minute)) 

    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

params = sys.stdin.readline().split()
a = int(params[0])
b = int(params[1])
h = int(params[2])
m = int(params[3])

print(distanceBetweenHands(h, m))
