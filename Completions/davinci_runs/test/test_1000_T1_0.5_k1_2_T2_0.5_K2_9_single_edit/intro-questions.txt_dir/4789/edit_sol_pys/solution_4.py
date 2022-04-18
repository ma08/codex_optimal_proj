
import sys
import fileinput

lines = fileinput.input()

k = int(sys.stdin.readline())
desks = list(map(int, sys.stdin.readline().split()))

# Sort the desks in ascending order
desks.sort()

# Find the minimum number of passes through the line
# by finding the maximum distance between two adjacent desk numbers
print(max(desks[i] - desks[i-1] for i in range(1, k)))
