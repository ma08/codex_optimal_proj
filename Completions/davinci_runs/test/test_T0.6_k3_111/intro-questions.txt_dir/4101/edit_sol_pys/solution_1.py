

# The idea is to keep track of the number of 1s in each column, and sort the rows based on the number of 1s in each row.
# If the number of 1s in the first row is greater than the number of 1s in the second row, invert the first row.
# If the number of 1s in the second row is greater than the number of 1s in the first row, invert the second row.
# If the number of 1s in the first row and second row are the same, then check the third row, and so on...
# The columns are sorted in the same way.
# If it is possible, then print "YES" and the rows and columns that were inverted.
# If not, then print "NO".

n, m = map(int, input().split())

# Create a 2D array that stores the number of 1s in each column
matrix = [[0 for i in range(m)] for j in range(n)]

# Store the number of 1s in each column
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())

# Create a 2D array that stores the number of 1s in each row
row_count = [[0 for i in range(m)] for j in range(n)]

# Store the number of 1s in each row
for i in range(n):
    for j in range(m):
        row_count[i][j] = matrix[i][j]

# Create a 2D array that stores the number of 1s in each column
column_count = [[0 for i in range(m)] for j in range(n)]

# Store the number of 1s in each column
for i in range(n):
    for j in range(m):
        column_count[j][i] = matrix[i][j]

# Sort the rows based on the number of 1s
for i in range(n - 1):
    for j in range(i + 1, n):
        if row_count[i][0] > row_count[j][0]:
            for k in range(m):
                row_count[i][k] = 1 - row_count[i][k]
        elif row_count[i][0] == row_count[j][0]:
            if row_count[i][1] > row_count[j][1]:
                for k in range(m):
                    row_count[i][k] = 1 - row_count[i][k]
            elif row_count[i][1] == row_count[j][1]:
                if row_count[i][2] > row_count[j][2]:
                    for k in range(m):
                        row_count[i][k] = 1 - row_count[i][k]
                elif row_count[i][2] == row_count[j][2]:
                    if row_count[i][3] > row_count[j][3]:
                        for k in range(m):
                            row_count[i][k] = 1 - row_count[i][k]
                    elif row_count[i][3] == row_count[j][3]:
                        if row_count[i][4] > row_count[j][4]:
                            for k in range(m):
                                row_count[i][k] = 1 - row_count[i][k]

# Sort the columns based on the number of 1s
for i in range(m - 1):
    for j in range(i + 1, m):
        if column_count[i][0] > column_count[j][0]:
            for k in range(n):
                column_count[i][k] = 1 - column_count[i][k]
        elif column_count[i][0] == column_count[j][0]:
            if column_count[i][1] > column_count[j][1]:
                for k in range(n):
                    column_count[i][k] = 1 - column_count[i][k]
            elif column_count[i][1] == column_count[j][1]:
                if column_count[i][2] > column_count[j][2]:
                    for k in range(n):
                        column_count[i][k] = 1 - column_count[i][k]
                elif column_count[i][2] == column_count[j][2]:
                    if column_count[i][3] > column_count[j][3]:
                        for k in range(n):
                            column_count[i][k] = 1 - column_count[i][k]
                    elif column_count[i][3] == column_count[j][3]:
                        if column_count[i][4] > column_count[j][4]:
                            for k in range(n):
                                column_count[i][k] = 1 - column_count[i][k]

# Check if the matrix is sorted
sorted = True
for i in range(n):
    for j in range(m):
        if matrix[i][j] != row_count[i][j]:
            sorted = False
            break
    if not sorted:
        break
if sorted:
    print("YES")
    for i in range(n):
        print(row_count[i][0], end = "")
    print()
    for i in range(m):
        print(column_count[i][0], end = "")
else:
    print("NO")
