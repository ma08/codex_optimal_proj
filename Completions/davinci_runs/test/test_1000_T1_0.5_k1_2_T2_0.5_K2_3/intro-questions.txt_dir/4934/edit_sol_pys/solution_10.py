import math

h, v = map(float, input().split())
print(int(round(h / math.sin(math.radians(v))))) 
