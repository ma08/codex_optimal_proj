

# Solution

# Number of files
n = int(input())
# Value of files
a = list(map(int, input().split()))

a.sort()

# To determine the minimum number of pockets, we will keep track of the last pocket assigned to each file value.

# Pocket number assigned to each file value
last_pocket = {}

# Number of pockets used
num_pockets = 0

for i in range(n):
    val = a[i]
    # If there is no pocket assigned to this value, assign a new pocket to the file
    if val not in last_pocket:
        last_pocket[val] = num_pockets
        num_pockets += 1
    # If there is a pocket assigned to this value, assign the next pocket to the file
    else:
        last_pocket[val] += 1

print(num_pockets)
