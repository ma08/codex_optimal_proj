

def playfair(key, plain_text):
    # Remove spaces, duplicate letters, and 'q'
    key = key.replace(" ", "")
    key = "".join(set(key))
    key = key.replace("q", "")

    # Add remaining letters
    alphabet = "abcdefghijklmnoprstuvwxyz"
    key += "".join(set(alphabet) - set(key))

    # Create table
    table = [''] * 5
    for i in range(5):
        table[i] = key[i*5:i*5+5]

    # Encrypt
    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        # Pad with 'x' if needed
        if i == len(plain_text) - 1:
            plain_text += 'x'
        elif plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i+1] + 'x' + plain_text[i+1:]

        # Get row and column of each letter
        row1, col1 = None, None
        row2, col2 = None, None
        for r in range(5):
            if plain_text[i] in table[r]:
                row1, col1 = r, table[r].index(plain_text[i])
            if plain_text[i + 1] in table[r]:
                row2, col2 = r, table[r].index(plain_text[i + 1])
        # Encrypt
        if row1 == row2:
            cipher_text += table[row1][(col1 + 1) % 5]
            cipher_text += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += table[(row1 + 1) % 5][col1]
            cipher_text += table[(row2 + 1) % 5][col2]
        else:
            cipher_text += table[row1][col2]
            cipher_text += table[row2][col1]


    return cipher_text.upper()

def main():
    key = input()
    plain_text = input()
    print(playfair(key, plain_text))

if __name__ == "__main__":
    main()
