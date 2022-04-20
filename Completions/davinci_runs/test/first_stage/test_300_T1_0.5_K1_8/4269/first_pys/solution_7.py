

import sys

# Get input from user
S = input()

# Compare adjacent digits
for i in range(0, 3):
    if S[i] == S[i+1]:
        print("Bad")
        sys.exit()

print("Good")