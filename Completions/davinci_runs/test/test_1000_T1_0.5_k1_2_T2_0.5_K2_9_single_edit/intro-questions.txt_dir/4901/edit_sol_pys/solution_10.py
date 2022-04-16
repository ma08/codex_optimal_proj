

def decrypt(msg):
    if len(msg) % 2 == 1:
        msg += 'A'

    msg1 = ''.join(chr((ord(c) - ord('A') + i) % 26 + ord('A')) for i, c in enumerate(msg[::2]))
    msg2 = ''.join(chr((ord(c) - ord('A') + i) % 26 + ord('A')) for i, c in enumerate(msg[1::2]))

    return ''.join(chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A')) for c1, c2 in zip(msg1, msg2))[:len(msg) // 2]

def main():
    msg = input()
    print(decrypt(msg))

if __name__ == '__main__':
    main()
