
# Get the input
n = int(input())
a = list(map(int, input().split()))[:n]

# Sort the list
a.sort()

# Check if the list has a unique maximum element
if a[-1] != a[-2]:
    # Find the index of the unique maximum element
    for i in range(n):
        if a[i] == a[-1]:
            print(i + 1)
            break
else:
    print("none")
