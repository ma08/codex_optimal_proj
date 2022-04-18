

import sys

# Read from stdin
H, W = map(int, sys.stdin.readline().split())
h, w = map(int, sys.stdin.readline().split())

# Solution
# All rows are either in the chosen rows or not.
# Same for columns.
# Thus, we can find the number of white cells in the chosen rows,
# and the number of white cells in the unchosen rows.
# Likewise for columns.
# The number of white cells remaining is the difference between the
# white cells in the chosen rows and the chosen columns, and the
# white cells in the unchosen rows and the unchosen columns.

# We want the number of white cells in the chosen rows and columns.
# Since we know the number of white cells in each row (W), and the number
# of rows in the chosen rows (h) and unchosen rows (H-h), we can use the
# formula for the sum of an arithmetic sequence to find the number of white
# cells in the chosen rows and unchosen rows.
# Likewise for columns.
# The number of white cells remaining is the difference between the
# white cells in the chosen rows and the chosen columns, and the
# white cells in the unchosen rows and the unchosen columns.

# White cells in rows
white_rows = h * W

# White cells in columns
white_columns = w * H

# Number of white cells
print(white_rows + white_columns)
