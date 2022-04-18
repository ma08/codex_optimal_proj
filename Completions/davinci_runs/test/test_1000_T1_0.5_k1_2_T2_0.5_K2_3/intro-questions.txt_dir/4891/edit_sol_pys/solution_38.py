import sys
pieces = [int(x) for x in sys.stdin.readline().split()]
print(1 - pieces[0], 1 - pieces[1], 2 - pieces[2], 2 - pieces[3], 2 - pieces[4], 8 - pieces[5])

