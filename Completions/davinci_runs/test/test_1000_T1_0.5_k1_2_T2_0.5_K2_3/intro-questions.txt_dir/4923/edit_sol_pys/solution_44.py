

# Get input
n = int(input())
a = list(map(int, input().split()))

# Sort the list
a.sort()

# Check if the list has a unique max element
if a[-1] != a[-2]:
    # Find the index of the unique max element
    for i in range(len(a)):
        if a[i] == a[-1]:
            print(i + 1)
            break
else:
    print("none")
