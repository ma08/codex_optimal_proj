
import sys


def decrypt(message, rows, columns):
    matrix = [[' '] * rows for _ in range(columns)]
    for i in range(len(message)):
        matrix[i // rows][i % rows] = message[i]
    return ''.join(c for row in matrix for c in row)


def main():
    message = sys.stdin.readline().strip()
    rows = int(sys.stdin.readline().strip())
    columns = int(sys.stdin.readline().strip())
    print(decrypt(message, rows, columns))


if __name__ == '__main__':
    main()
