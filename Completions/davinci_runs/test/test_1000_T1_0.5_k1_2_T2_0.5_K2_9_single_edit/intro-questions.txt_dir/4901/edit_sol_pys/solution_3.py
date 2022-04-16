
#!/usr/bin/env python3

def decrypt(msg):
    msg = list(msg)
    msg.sort()
    msg = ''.join(msg)

    for i in range(26):
        rotation = i

        msg1 = ''.join(chr((ord(c) - ord('A') + rotation) % 26 + ord('A')) for c in msg)

        if 'THE' in msg1 and 'AND' in msg1:
            return msg1

    print(msg1, msg2)


def main():
    msg = input()
    print(decrypt(msg))

if __name__ == '__main__':
    main()
