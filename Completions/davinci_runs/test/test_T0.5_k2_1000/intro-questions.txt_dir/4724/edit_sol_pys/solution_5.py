
# read input
import sys

r = int(sys.stdin.readline().rstrip()) # red
g = int(sys.stdin.readline().rstrip()) # green

print(int(g + (g-r)/2))
