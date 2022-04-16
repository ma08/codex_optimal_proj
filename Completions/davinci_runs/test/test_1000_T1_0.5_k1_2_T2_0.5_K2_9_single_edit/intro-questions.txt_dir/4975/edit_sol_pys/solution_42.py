

import sys

def main():
    key = sys.stdin.readline()
    key_table = build_key_table(key)
    plaintext = sys.stdin.readline()
    ciphertext = encrypt(key_table, plaintext)
    print(ciphertext)

def build_key_table(key):
    key_table = [[None for _ in range(5)] for _ in range(5)]
    key_set = set()
    row = 0
    col = 0

    for char in key:
        if char == ' ':
            continue
        if char == 'q':
            continue
        if char in key_set:
            continue
        key_set.add(char)
        key_table[row][col] = char
        col += 1
        if col == 5:
            row += 1
            col = 0

    for char in 'abcdefghiklmnoprstuvwxyz':
        if char in key_set:
            continue
        key_set.add(char)
        key_table[row][col] = char
        col += 1
        if col == 5:
            row += 1
            col = 0

    return key_table

def encrypt(key_table, plaintext):
    ciphertext = ''
    plaintext = ''.join(plaintext.split())
    plaintext = add_x_if_needed(plaintext)

    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]
        ciphertext += encrypt_pair(key_table, pair)

    return ciphertext.upper()

def encrypt_pair(key_table, pair):
    assert len(pair) == 2
    assert pair[0] != pair[1]
    if pair[0] == 'q':
        pair = 'x' + pair[1]
    if pair[1] == 'q':
        pair = pair[0] + 'x'

    row1, col1 = find_char_in_key_table(key_table, pair[0])
    row2, col2 = find_char_in_key_table(key_table, pair[1])

    if row1 == row2:
        return key_table[row1][(col1+1)%5] + key_table[row2][(col2+1)%5]
    elif col1 == col2:
        return key_table[(row1+1)%5][col1] + key_table[(row2+1)%5][col2]
    else:
        return key_table[row1][col2] + key_table[row2][col1]

def find_char_in_key_table(key_table, char):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return (row, col)
    raise RuntimeError('char not found in key_table')

def add_x_if_needed(plaintext):
    for i in range(0, len(plaintext)-1):
        if plaintext[i] == 'x' and plaintext[i+1] == 'x':
            plaintext = plaintext[:i+1] + 'q' + plaintext[i+1:]
    if plaintext[-1] == 'x':
        plaintext = plaintext + 'q'
    return plaintext

if __name__ == '__main__':
    main()
