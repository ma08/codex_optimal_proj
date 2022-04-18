# Read the input
n = int(input())
e = list(map(int, input().split()))

# Base case for n = 1
if n == 1:
    print(e[0])

# Base case for n = 2
elif n == 2:
    print(max(e[0], e[1]))

# Base case for n = 3
elif n == 3:
    print(max(e[0], e[1], e[2]))

# Base case for n = 4
elif n == 4:
    print(max(e[0]+e[2], e[1]+e[3]))

# General case
else:
    # Sort the list
    e.sort()

    # The maximum value is the sum of the largest two even numbers and the
    # largest odd number
    print(e[-1]+e[-3]+e[-5])
