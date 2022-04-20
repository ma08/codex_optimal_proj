

from sys import stdin

x, y = map(int, stdin.readline().rstrip().split())
if y % 2 == 1 or x * 2 > y or y > 4 * x:
    print("No")
else:
    print("Yes")