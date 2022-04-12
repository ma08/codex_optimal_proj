

def main():
    ciphertext = input()
    ciphertext_length = len(ciphertext)
    half_ciphertext_length = int(ciphertext_length / 2)
    half_ciphertext_1 = ciphertext[:half_ciphertext_length]
    half_ciphertext_2 = ciphertext[half_ciphertext_length:]

    half_ciphertext_1_rotation = 0
    half_ciphertext_2_rotation = 0

    for ciphertext_char in half_ciphertext_1:
        half_ciphertext_1_rotation += ord(ciphertext_char) - 65
    for ciphertext_char in half_ciphertext_2:
        half_ciphertext_2_rotation += ord(ciphertext_char) - 65

    half_ciphertext_1_rotation = half_ciphertext_1_rotation % 26
    half_ciphertext_2_rotation = half_ciphertext_2_rotation % 26

    half_ciphertext_1_rotated = ""
    half_ciphertext_2_rotated = ""

    for ciphertext_char in half_ciphertext_1:
        half_ciphertext_1_rotated += chr((ord(ciphertext_char) - 65 + half_ciphertext_1_rotation) % 26 + 65)
    for ciphertext_char in half_ciphertext_2:
        half_ciphertext_2_rotated += chr((ord(ciphertext_char) - 65 + half_ciphertext_2_rotation) % 26 + 65)

    plaintext = ""

    for i in range(half_ciphertext_length):
        plaintext += chr((ord(half_ciphertext_1_rotated[i]) - 65 + ord(half_ciphertext_2_rotated[i]) - 65) % 26 + 65)

    print(plaintext)

if __name__ == '__main__':
    main()
