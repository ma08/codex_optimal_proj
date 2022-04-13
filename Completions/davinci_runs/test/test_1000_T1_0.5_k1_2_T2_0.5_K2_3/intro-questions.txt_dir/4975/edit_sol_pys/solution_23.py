

def playfair(key, plaintext):
    # Remove spaces, duplicate letters, and 'Q'
    key = key.replace(' ', '')
    key = ''.join(set(key))
    key = key.replace('Q', '')

    # Add remaining letters
    alphabet = "abcdefghijklmnoprstuvwxyz"
    key += "".join(set(alphabet) - set(key))

    # Create table
    table = [''] * 5
    for i in range(5):
        table[i] = key[i*5:i*5+5]

    # Encrypt
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        # Pad with 'x' if needed
        if i == len(plaintext) - 1:
            plaintext += 'x'
        elif plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + 'x' + plaintext[i+1:]

        # Get row and column of each letter
        row1, col1 = None, None
        row2, col2 = None, None
        for r in range(5):
            if plaintext[i] in table[r]:
                row1, col1 = r, table[r].index(plaintext[i])
            if plaintext[i+1] in table[r]:
                row2, col2 = r, table[r].index(plaintext[i+1])
        # Encrypt
        if row1 == row2:
            ciphertext += table[row1][(col1+1)%5]
            ciphertext += table[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[(row1+1)%5][col1]
            ciphertext += table[(row2+1)%5][col2]
        else:
            ciphertext += table[row1][col2]
            ciphertext += table[row2][col1]

    return ciphertext.upper()

def main():
    key = input()
    plaintext = input()
    print(playfair(key, plaintext))

if __name__ == "__main__":
    main()
