
import fileinput

lines = fileinput.input(files=('input.txt'))

k = int(lines[0])
desks = list(map(int, lines[1:]))

# Sort the desks in ascending order
desks.sort()

# Find the minimum number of passes through the line
# by finding the maximum distance between two adjacent desk numbers
print(max(desks[i] - desks[i-1] for i in range(1, k+1)))
