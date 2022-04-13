

def decrypt(enc):
    enc_len = len(enc)
    half = enc_len // 2
    enc1 = enc[:half]
    enc2 = enc[half:]
    print(enc1, enc2)

    rotation1 = 0
    for c in enc1:
        rotation1 += ord(c) - ord('A')
    rotation1 %= 26

    rotation2 = 0
    for c in enc2:
        rotation2 += ord(c) - ord('A')
    rotation2 %= 26

    enc1 = ''.join(chr((ord(c) - ord('A') - rotation1) % 26 + ord('A')) for c in enc1)
    enc2 = ''.join(chr((ord(c) - ord('A') - rotation2) % 26 + ord('A')) for c in enc2)

    print(enc1, enc2)

    return ''.join(chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A')) for c1, c2 in zip(enc1, enc2))

def main():
    enc = input()
    print(decrypt(enc))

if __name__ == '__main__':
    main()
