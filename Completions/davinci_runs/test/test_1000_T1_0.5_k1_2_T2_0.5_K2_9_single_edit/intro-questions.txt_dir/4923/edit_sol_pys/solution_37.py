

# Read input
n = int(input())
a = list(map(int, input().split()))

# Check if all numbers are the same
unique_numbers = set(a)
if len(unique_numbers) == 1:
    print("none")

# Check if all numbers are not the same
else:
    # Find the highest unique number
    for i in range(6, 0, -1):
        if i in unique_numbers:
            highest_unique = i
            break

    # Find the index of the highest unique number
    for i in range(n):
        if a[i] == highest_unique:
            print(i + 1)
            break
