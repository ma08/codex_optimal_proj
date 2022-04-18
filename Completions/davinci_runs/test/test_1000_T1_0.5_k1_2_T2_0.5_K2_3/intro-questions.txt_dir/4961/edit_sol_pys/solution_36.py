
import sys
lines = sys.stdin.readlines()
R, S = [int(x) for x in lines[0].split()]

seating = [list(s.strip()) for s in lines[1:]]
print(seating)
