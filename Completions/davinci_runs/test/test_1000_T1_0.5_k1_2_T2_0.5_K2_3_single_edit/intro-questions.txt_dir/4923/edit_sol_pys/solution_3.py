
# Read input
n = int(input())
a = list(map(int, input().split()))

# Check if there are any unique numbers
if len(set(a)) != 1:
    # Find the highest unique number
    for i in range(6, 0, -1):
        if i in a:
            highest_unique = i
            break

    # Find the index of the highest unique number
    for i in range(n):
        if a[i] == highest_unique:
            print(i + 1)
            break

# Check if there are any unique numbers
else:
    print("none")
