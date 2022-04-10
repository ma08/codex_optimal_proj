

# Code Section

def getMinDivisions(array: list, equalNumbers: int) -> int:
    """
    We need to find the minimum number of divisions to be done to get
    equal numbers.

    A division can be done only on an odd number, as even numbers will
    divide down to even numbers.

    We need to find the maximum number of odd numbers in the array, as
    they will be the ones that will be divided.

    We can divide a number by 2, till it's odd.
    """

    # This is the count of odd numbers
    oddNumbers = 0

    # Iterate the array
    for number in array:

        # If the number is odd, increment
        if number % 2 == 1:
            oddNumbers += 1

    # If there are no odd numbers, we can't divide
    if oddNumbers == 0:
        return 0

    # If the odd numbers are less than the required equal numbers,
    # then we can't divide
    if oddNumbers < equalNumbers:
        return -1

    # The minimum number of divisions is the difference of the odd
    # numbers and the required equal numbers
    return oddNumbers - equalNumbers


# Read the number of elements and the number of equal numbers
arraySize, equalNumbers = [int(x) for x in input().split()]

# Read the array
array = [int(x) for x in input().split()]

# Get the minimum number of divisions
minDivisions = getMinDivisions(array, equalNumbers)

# Print the result
if minDivisions == -1:
    print("IMPOSSIBLE")
else:
    print(minDivisions)