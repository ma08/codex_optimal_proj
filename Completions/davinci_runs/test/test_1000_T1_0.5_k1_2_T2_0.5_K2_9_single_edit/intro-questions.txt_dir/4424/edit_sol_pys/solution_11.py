
import sys

k, x = [int(i) for i in sys.stdin.readline().split()]

if (500 * k) >= x:
    print("Yes")
else:
    print("No")
