

# read input
a, b = list(map(int, input().split()))

# check if any part of the window is uncovered
if a <= b:
    print(0)
else:
    print(a-b)