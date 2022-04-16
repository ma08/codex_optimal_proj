def decrypt(msg):
    msg_len = len(msg)
    half = msg_len // 2
    msg1 = msg[:half]
    msg2 = msg[half:]
    print(msg1, msg2)

    rotation1 = 0
    for c in msg1:
        rotation1 += ord(c) - ord('A')
    rotation1 %= 26

    rotation2 = 0
    for c in msg2:
        rotation2 += ord(c) - ord('A')
    rotation2 %= 26

    msg1 = ''.join(chr((ord(c) - ord('A') + rotation1) % 26 + ord('A')) for c in msg1)
    msg2 = ''.join(chr((ord(c) - ord('A') + rotation2) % 26 + ord('A')) for c in msg2)

    print(msg1, msg2)

    return ''.join(chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A')) for c1, c2 in zip(msg1, msg2))


def main():
    msg = input()
    print(decrypt(msg))


if __name__ == '__main__':
    main()



def decrypt(msg):
    msg_len = len(msg)
    half = msg_len // 2
    msg1 = msg[:half]
    msg2 = msg[half:]
    print(msg1, msg2)

    rotation1 = 0
    for c in msg1:
        rotation1 += ord(c) - ord('A')
    rotation1 %= 26

    rotation2 = 0
    for c in msg2:
        rotation2 += ord(c) - ord('A')
    rotation2 %= 26

    msg1 = ''.join(chr((ord(c) - ord('A') + rotation1) % 26 + ord('A')) for c in msg1)
    msg2 = ''.join(chr((ord(c) - ord('A') + rotation2) % 26 + ord('A')) for c in msg2)

    print(msg1, msg2)

    return ''.join(chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A')) for c1, c2 in zip(msg1, msg2))

def main():
    msg = input()
    print(decrypt(msg))

if __name__ == '__main__':
    main()
