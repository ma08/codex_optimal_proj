

n = int(input('Enter the number of elements in the array: '))
t = list(map(int, input('Enter the elements of the array: ').split()))

# Sort the temperatures
t.sort()

# Base case for n = 1.
if n == 1:
    print(t[0])

# Base case for n = 2.
elif n == 2:
    print(t[1], t[0], sep=' ')

# General case.
else:
    if t[-1] - t[0] < t[1] - t[0] and n > 2:
        print('Impossible')

    # If the input is possible.
    else:
        print(t[-1], end=' ')  # Print the largest element.
        for i in range(1, n-1):  # Print the remaining elements in the array.
            print(t[i], end=' ')  # Print the remaining elements in the array.
        print(t[0])  # Print the smallest element.
