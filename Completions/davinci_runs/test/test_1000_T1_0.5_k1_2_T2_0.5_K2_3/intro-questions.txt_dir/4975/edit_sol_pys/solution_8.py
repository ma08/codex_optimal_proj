

    plaintext = plaintext.upper()
def encrypt(key, plaintext):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("Q", "") #remove all Q
    plaintext = plaintext.replace("J", "") #remove all J
    plaintext = plaintext.replace("X", "")
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)] #split the plaintext into 2-letter words
    for i in range(len(plaintext)):
        if len(plaintext[i]) == 1: #if there's only 1 letter, add a X
            plaintext[i] += "X"
        if plaintext[i][0] == plaintext[i][1]: #if 2 letters are the same, add a X
            plaintext[i] = plaintext[i][0] + "X"
    ciphertext = ""
    for i in range(len(plaintext)):
        row1, col1 = key.index(plaintext[i][0]) // 5, key.index(plaintext[i][0]) % 5
        row2, col2 = key.index(plaintext[i][1]) // 5, key.index(plaintext[i][1]) % 5
        if row1 == row2:
            ciphertext += key[row1 * 5 + (col1 + 1) % 5] + key[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key[((row1 + 1) % 5) * 5 + col1] + key[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += key[row1 * 5 + col2] + key[row2 * 5 + col1]
    return ciphertext

key = input()
plaintext = input()
key = key.upper()
key = key.replace(" ", "") #remove spaces
key = key.replace("Q", "")
key = key.replace("J", "")
key = key.replace("X", "")
key = [key[i:i+2] for i in range(0, len(key), 2)]
key = list(set(key))
key = sorted(key)
key = "".join(key)
key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = key[:25]
print(encrypt(key, plaintext))
