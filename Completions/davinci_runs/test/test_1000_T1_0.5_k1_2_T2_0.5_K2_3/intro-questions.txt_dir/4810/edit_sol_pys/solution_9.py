#!/usr/bin/env python3

import sys

def decrypt(message):
    message_len = len(message)
    rows = 1
    while rows * rows < message_len:
        rows += 1
    columns = message_len // rows
    if rows * columns < message_len:
        columns += 1
    matrix = [[' '] * columns for _ in range(rows)]
    for i in range(message_len):
        matrix[i % rows][i // rows] = message[i]
    return ''.join(c for row in matrix for c in row if c != ' ') + '\n'

def main():
    message = sys.stdin.readline().strip()
    print(decrypt(message))

if __name__ == '__main__':
    main()
