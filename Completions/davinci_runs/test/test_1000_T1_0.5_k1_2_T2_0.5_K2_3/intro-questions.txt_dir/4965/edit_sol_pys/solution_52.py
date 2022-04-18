# Read input

n = int(input())
t = list(map(int, input().split()))

# Sort the temperatures
t.sort()

# Base case for n = 2
if n == 2:
    print(t[1], end=' ')
    print(t[0])

# Base case for n = 3
elif n == 3:
    print(t[2], end=' ')
    print(t[0], end=' ')
    print(t[1])

# General case
else:
    # If the input is impossible
    if t[-1] - t[0] < t[1] - t[0]:
        print('impossible')

    # If the input is possible
    else:
        print(t[-1], end=' ')
        for i in range(1, n-1):
            print(t[i], end=' ')
        print(t[0])
