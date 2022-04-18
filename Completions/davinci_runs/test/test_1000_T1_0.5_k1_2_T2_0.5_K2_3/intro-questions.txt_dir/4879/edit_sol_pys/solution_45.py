
import sys

a, b, c = sys.stdin.readline().split()

if a == "North" and (b == "West" and c == "East") or (b == "East" and c == "West") or \
        a == "South" and (b == "West" and c == "East") or (b == "East" and c == "West") or \
        a == "East" and (b == "North" and c == "South") or (b == "South" and c == "North") or \
        a == "West" and (b == "North" and c == "South") or (b == "South" and c == "North"):
    print("Yes")
else:
    print("No")
