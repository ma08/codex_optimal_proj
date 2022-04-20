
import sys

n = int(sys.stdin.readline())

if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("Yes")
else:
    print("No")
