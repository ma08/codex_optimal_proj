import sys

N = sys.stdin.readline()

if int(N) % 2 == 0 or int(N) % 3 == 0 or int(N) % 5 == 0 or int(N) % 7 == 0:
    print("Yes")
else:
    print("No")
