

# -----CODE-----
# Read in STDIN
n, q = map(int, input().split())
s = input()

# Initialize variables
ac_count = 0

# Go through string, counting how many pairs of A and C in the string
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        ac_count += 1

# Initialize running count of AC pairs
running_ac_count = ac_count

# Go through queries
for i in range(q):
    l, r = map(int, input().split())

    # Check if we need to remove any AC pairs from left side
    if s[l - 2] == 'A' and s[l - 1] == 'C':
        running_ac_count -= 1
    # Check if we need to add any AC pairs from right side
    if s[r - 1] == 'A' and s[r] == 'C':
        running_ac_count += 1

    print(running_ac_count)
