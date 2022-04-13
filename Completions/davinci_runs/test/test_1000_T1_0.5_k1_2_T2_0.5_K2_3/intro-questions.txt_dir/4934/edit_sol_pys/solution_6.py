import sys
import math

height, angle = map(int, sys.stdin.readline().split())

print(math.ceil(height / math.sin(math.radians(angle))))
