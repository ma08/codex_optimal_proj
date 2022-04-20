

import sys

# Read the input
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

# Count the number of differences
count = 0
for i in range(0, len(s)):
    if s[i] != t[i]:
        count += 1

# Print the result
print(count)