
from __future__ import print_function
# Get Input
a1, a2, a3 = map(int, input().split())

# Check if Bust
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
