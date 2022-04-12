import math

x, y, x1, y1, x2, y2 = map(int, input().split()) # Read input

dx = min(abs(x-x1), abs(x-x2)) # Find the distances to the sides of the rectangle
dy = min(abs(y-y1), abs(y-y2)) # Find the distances to the sides of the rectangle

print(math.sqrt(dx*dx + dy*dy)) # Print the minimum distance
