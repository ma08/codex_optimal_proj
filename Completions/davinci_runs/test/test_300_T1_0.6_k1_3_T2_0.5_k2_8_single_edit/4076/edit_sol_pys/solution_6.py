

import sys
import math

def distanceBetweenHands(hour, minute):
    hourAngle = hour * 30.0
    minuteAngle = minute * 6.0

    x1 = 3.0 * math.cos(math.radians(hourAngle))
    y1 = 3.0 * math.sin(math.radians(hourAngle))
    x2 = 4.0 * math.cos(math.radians(minuteAngle))
    y2 = 4.0 * math.sin(math.radians(minuteAngle))

    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

params = sys.stdin.readline().split()
a = int(params[0])
b = int(params[1])
h = int(params[2])
m = int(params[3])

print(distanceBetweenHands(h, m))
