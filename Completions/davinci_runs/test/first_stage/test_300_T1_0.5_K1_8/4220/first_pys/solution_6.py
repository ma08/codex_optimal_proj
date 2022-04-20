

# Import
import sys

# Define Functions
def abridged_string(k, s):
    if len(s) > k:
        return s[:k] + "..."
    else:
        return s

# Main
k = int(input())
s = input()
print(abridged_string(k, s))