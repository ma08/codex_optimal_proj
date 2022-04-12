

# The number of cuts is the number of rectangles.
# So the maximum number of pieces is the number of rectangles plus one.
# The number of rectangles is the sum of the number of rectangles in each row and column.
# The number of rectangles in each row and column is the number of rectangles in the first row/column plus the number of rectangles in the second row/column plus... etc.
# The number of rectangles in the first row/column is 1.
# The number of rectangles in the second row/column is 2.
# ... etc.
# The number of rectangles in the nth row/column is n.
# The sum of the first n natural numbers is n(n+1)/2.
# So the number of rectangles is n(n+1).
# So the maximum number of pieces is n(n+1)+1.

import sys

n = int(sys.stdin.readline())

print(n*(n+1)+1)
