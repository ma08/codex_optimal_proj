

def encrypt(key, plaintext):
    plaintext = plaintext.replace(" ", "").upper().replace("Q", "").replace("J", "").replace("X", "")
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2) if plaintext[i:i+2] != ""]
    for i in range(len(plaintext)):
        if len(plaintext[i]) == 1:
            plaintext[i] += "X"
        if plaintext[i][0] == plaintext[i][1]:
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
key = key.replace(" ", "").upper().replace("Q", "").replace("J", "").replace("X", "")
key = [key[i:i+2] for i in range(0, len(key), 2) if key[i:i+2] != ""]
key = list(set(key))
key = sorted(key)
key = "".join(key)
key = key.replace("I", "")
key = key.replace("U", "")
key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = key[:25]
print(encrypt(key, plaintext))
