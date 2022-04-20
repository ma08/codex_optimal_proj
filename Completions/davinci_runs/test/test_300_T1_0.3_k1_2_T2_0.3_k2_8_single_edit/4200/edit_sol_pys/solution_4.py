#!/usr/bin/env python3

# Read input
n, m = map(int, input().split())
votes = list(map(int, input().split()))

# Check if the most popular item has enough votes
if max(votes) >= (sum(votes) / (4 * m)):
    print("Yes")
else:
    print("No")
