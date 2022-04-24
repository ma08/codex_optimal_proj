
import sys

line = sys.stdin.readline().strip().split()  # strip() removes trailing \n

print(int(float(line[0]) * float(line[1])))  # float() returns a floating point number
