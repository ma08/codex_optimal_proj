
# Get input
n = int(input())
a = list(map(int, input().split()))

# Sort the list
a.sort()

# Check if the list has a unique max or min element
if a[-1] != a[-2] or a[0] != a[1]:
    # Find the index of the unique max or min element
    for i in range(n):
        if a[i] == a[-1] or a[i] == a[0]:
            print(i + 1)

            break
else:
    print("None")
