

# The number of cuts is the number of squares plus one.
# So the maximum number of pieces is the number of squares plus one.
# The number of squares is the sum of the number of squares in each row and column.
# The number of squares in each row and column is the number of squares in the first row/column plus the number of squares in the second row/column plus...(and so on)
# The number of squares in the first row/column is 1.
# The number of squares in the second row/column is 2.
# ...
# The number of squares in the nth row/column is n.
# The sum of the first n natural numbers is n(n+1)/2.
# So the number of squares is n(n+1).
# So the maximum number of pieces is n(n+1)+1.

import sys

n = int(sys.stdin.readline())

print(n*(n+1)+1)
