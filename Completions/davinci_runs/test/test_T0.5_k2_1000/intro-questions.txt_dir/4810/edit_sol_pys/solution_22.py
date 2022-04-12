

message = input("Enter a message: ")

# Get the length of the message
length = len(message)

# Get the square root of the length of the message
sqrt = int(length ** 0.5)

# Get the number of rows and columns
rows = sqrt
columns = sqrt

# If the number of rows times the number of columns is not equal to the length of the message,
# increment the number of rows by 1 and decrement the number of columns by 1
# until the number of rows times the number of columns is equal to the length of the message
if rows * columns < length:
    rows += 1
    if rows * columns < length:
        columns += 1

# Create a matrix with the number of rows and columns
matrix = [[0 for x in range(columns)] for y in range(rows)]

# Create a counter for the message
counter = 0

# For each row and column in the matrix, place the character at the counter in the message
# in the matrix and increment the counter by 1
for row in range(rows):
    for column in range(columns):
        matrix[row][column] = message[counter]
        counter += 1

# Create a new string
newString = ""

# For each column in the matrix, for each row in the matrix, add the character
# at the row and column in the matrix to the new string
for column in range(columns):
    for row in range(rows):
        if matrix[row][column] != 0:
            newString += matrix[row][column]

# Print the new string
print(newString)
