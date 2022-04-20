

# X is the number we are trying to find the closest to
# N is the length of the sequence
# p_1, ..., p_N is the sequence

x, n = input().split()
x = int(x)
n = int(n)

p = input().split()
p = [int(i) for i in p]

# First, we create a list with all the numbers between 1 and 100 (inclusive)
# We then remove all the numbers that are in the sequence p_1, ..., p_N
# This way, we are left with a list of all the numbers that are not in the sequence

all_numbers = list(range(1, 101))
for i in p:
    all_numbers.remove(i)

# Next, we sort the list all_numbers.
# This allows us to use binary search to find the closest number to x

all_numbers.sort()

# If x is smaller than the first number in all_numbers, then the closest number to x is the first number in all_numbers
# If x is greater than the last number in all_numbers, then the closest number to x is the last number in all_numbers
# Otherwise, we use binary search to find the closest number to x

if x < all_numbers[0]:
    print(all_numbers[0])
elif x > all_numbers[-1]:
    print(all_numbers[-1])
else:
    # The following code is a modified version of binary search
    # The modification is that instead of returning the index of the number we are looking for,
    # it returns the index of the closest number to the number we are looking for
    # We start by assuming that the closest number is at the beginning of all_numbers
    # We then change the value of the closest number if we find a number that is closer
    # We repeat this until we find the number we are looking for or we have narrowed our search down to one number

    closest_number = 0
    left = 0
    right = len(all_numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if all_numbers[mid] < x:
            # If all_numbers[mid] < x, then we want to look at the numbers after all_numbers[mid]
            # Check if all_numbers[mid] is closer than the closest number we have found so far
            if abs(x - all_numbers[mid]) < abs(x - all_numbers[closest_number]):
                closest_number = mid
            left = mid + 1
        elif all_numbers[mid] > x:
            # If all_numbers[mid] > x, then we want to look at the numbers before all_numbers[mid]
            # Check if all_numbers[mid] is closer than the closest number we have found so far
            if abs(x - all_numbers[mid]) < abs(x - all_numbers[closest_number]):
                closest_number = mid
            right = mid
        else:
            # If all_numbers[mid] == x, then we have found the number we are looking for
            print(x)
            exit()
    # If we reach this point, then we have narrowed our search down to one number
    # This number is the closest number to the number we are looking for
    print(all_numbers[closest_number])