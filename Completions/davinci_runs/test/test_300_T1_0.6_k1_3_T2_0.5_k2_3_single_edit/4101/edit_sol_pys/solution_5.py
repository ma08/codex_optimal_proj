

from collections import Counter

n, m = map(int, input().split())
m = [[int(i) for i in input().split()] for _ in range(n)]

# if a row is sorted, mark it as "good"
# if a row is not sorted, mark it as "bad"
# if a column has 0s, mark it as "bad"
# if a column has 1s, mark it as "good"
# if a column has both 0s and 1s, mark it as "bad"

# after finding all the good and bad rows and columns,
# we can do the following:
# if there are more than 1 "good" row,
# we can invert any of them to make it "bad"
# if there are more than 1 "good" column,
# we can invert any of them to make it "bad"
# if there are more than 1 "bad" row and
# more than 1 "bad" column, we cannot sort the matrix
# if there are more than 1 "bad" row and 0 "bad" column,
# we can invert any of the "bad" rows to make it "good"
# if there are more than 1 "bad" column and 0 "bad" row,
# we can invert any of the "bad" columns to make it "good"
# if there is 1 "bad" row and 1 "bad" column,
# we can invert any 1 of them to make it "good"

good_rows = []
good_cols = []
bad_rows = []
bad_cols = []

for i in range(n):
    if all(m[i]):
        good_rows.append(i)
    elif not any(m[i]):
        bad_rows.append(i)

for j in range(n):
    if not any(m[i][j] for i in range(n)):
        bad_cols.append(j)
    elif all(m[i][j] for i in range(n)):
        good_cols.append(j)

if len(good_rows) > 1 or len(good_cols) > 1:
    print("YES")
    print("0" * m)
    print("0" * n)
elif len(bad_rows) > 1 and len(bad_cols) > 1:
    print("NO")
elif len(bad_rows) > 1:
    print("YES")
    print("0" * m)
    print("0" * n)
elif len(bad_cols) > 1:
    print("YES")
    print("0" * m)
    print("0" * n)
else:
    print("YES")
    print("0" * n)
    print("0" * m)
