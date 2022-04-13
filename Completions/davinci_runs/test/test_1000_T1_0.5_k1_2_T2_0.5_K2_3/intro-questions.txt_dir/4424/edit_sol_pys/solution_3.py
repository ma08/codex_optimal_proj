import sys

k, x = [int(i) for i in sys.stdin.readline().split()]

print("Yes" if (500 * k) >= x else "No")
