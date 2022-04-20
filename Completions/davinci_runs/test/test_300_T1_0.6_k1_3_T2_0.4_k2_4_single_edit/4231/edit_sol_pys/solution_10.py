
import sys

# Read from stdin.
H, W = map(int, sys.stdin.readline().split())  # Number of rows and columns.
h, w = map(int, sys.stdin.readline().split())  # Number of rows and columns in the chosen rectangle.

# Solution.
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

# White cells in chosen rows.
chosen_rows = h * W

# White cells in unchosen rows.
unchosen_rows = (H - h) * W

# White cells in chosen columns.
chosen_columns = w * H

# White cells in unchosen columns.
unchosen_columns = (W - w) * H

# Number of white cells remaining.
print(chosen_rows + chosen_columns - unchosen_rows - unchosen_columns)
