

import math
h, v = map(int, input().split())  # h is the height of the ladder and v is the angle
print(int(round(h / math.sin(math.radians(v)))))  # print the length of the ladder
