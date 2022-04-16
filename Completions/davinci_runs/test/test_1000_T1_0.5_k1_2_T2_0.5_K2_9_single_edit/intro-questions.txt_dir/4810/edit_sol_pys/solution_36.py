import sys

def decrypt(message):
    message_len = len(message)
    rows = 1
    while rows * rows < message_len: # find the number of rows
        rows += 1
    columns = message_len // rows # find the number of columns
    if rows * columns < message_len: # if the number of rows * columns is smaller than message length, add 1 to columns
        columns += 1
    matrix = [[' '] * columns for _ in range(rows)] # create a matrix
    for i in range(message_len):
        matrix[i % rows][i // rows] = message[i]
    return ''.join(c for row in matrix for c in row if c != ' ')

def main():
    message = sys.stdin.readline().strip()
    print(decrypt(message))

if __name__ == '__main__':
    main()
