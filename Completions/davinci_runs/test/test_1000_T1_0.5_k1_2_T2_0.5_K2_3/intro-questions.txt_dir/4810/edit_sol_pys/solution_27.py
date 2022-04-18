

message = input()

def encode(message):
    # Get the length of the message
    length = len(message)

    # Get the square root of the length of the message
    sqrt = length ** 0.5

    # Get the next lowest integer value of sqrt.
    rows = int(sqrt)

    # Get the next highest integer value of sqrt.
    columns = int(sqrt) + 1

    # If the number of rows times the number of columns is not equal to the length of the message, increment the number of rows by 1 and decrement the number of columns by 1 until the number of rows times the number of columns is equal to the length of the message.
    while rows * columns != length:
        if rows * columns < length:
            rows += 1
        else:
            columns -= 1

    # Create a matrix with the number of rows and columns.
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
            newString += matrix[row][column]

    # Print the new string
    print(newString)


encode(message)
