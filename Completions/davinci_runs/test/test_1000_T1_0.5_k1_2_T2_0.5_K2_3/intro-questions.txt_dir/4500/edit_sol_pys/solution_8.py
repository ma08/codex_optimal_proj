#!/usr/bin/env python3

# Read input
A, B, C = map(int, input().split())

# Check if he can buy the toys
if A + B >= C:
    print("Yes")
else:
    print("No")
