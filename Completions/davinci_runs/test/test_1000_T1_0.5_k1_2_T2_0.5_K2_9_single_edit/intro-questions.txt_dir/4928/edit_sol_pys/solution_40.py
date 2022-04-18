

# The number of cuts is the number of squares.
# So the maximum number of pieces is the number of squares plus one.
# The number of squares is the sum of the number of squares in each row and the number of squares in each column.
# The number of squares in each row is the number of squares in the first row plus the number of squares in the second row plus...
# The number of squares in each column is the number of squares in the first column plus the number of squares in the second column plus...
# The number of squares in the first row is 1.
# The number of squares in the second row is 2.
# The number of squares in the first column is 1.
# The number of squares in the second column is 2.
# ...
# The number of squares in the nth row is n.
# The number of squares in the nth column is n.
# The sum of the first n natural numbers is n(n+1)/2.
# So the number of squares is n(n+1).
# So the maximum number of pieces is n(n+1)+1.

import sys

n = int(sys.stdin.readline())

print(n*(n+1)+1)
