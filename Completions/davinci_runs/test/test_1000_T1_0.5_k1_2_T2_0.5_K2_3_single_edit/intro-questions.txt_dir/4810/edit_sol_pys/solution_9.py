# Get the message

message = input()

# Get the length of the message
length = len(message)

# Get the square root of the length of the message and round it down
sqrt = length ** 0.5

# Get the next lowest integer value of sqrt to get the number of rows
rows = int(sqrt)

# Get the next highest integer value of sqrt to get the number of columns
columns = int(sqrt) + 1

# If the number of rows times the number of columns is less than the length of the message
if rows * columns < length:
    # Increment the number of rows by 1
    rows += 1

    # If the number of rows times the number of columns is still less than the length of the message
    if rows * columns < length:
        # Increment the number of columns by 1
        columns += 1

# Create a matrix with the number of rows and columns
matrix = [[0 for x in range(columns)] for y in range(rows)]

# Create a counter for the message and set it equal to 0
counter = 0

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
            matrix[row][column] = message[counter]
            counter += 1

# For each row in the matrix
for row in range(rows):
    # For each column in the matrix
    for column in range(columns):
        # If the counter is not equal to the length of the message
        if counter != length:
            # Place the character at the counter in the message in the matrix and increment the counter by 1
        matrix[row][column] = message[counter]
        counter += 1

# Create a new string
newString = ""

# For each column in the matrix, for each row in the matrix, add the character
# at the row and column in the matrix to the new string
for column in range(columns):
    for row in range(rows):
        newString += matrix[row][column]

# Print the new string
print(newString)
