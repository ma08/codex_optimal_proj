

def encrypt(msg):
    msg_len = len(msg)  # length of the message
    half = msg_len // 2  # half of the message
    msg1 = msg[:half]  # first half of the message
    msg2 = msg[half:]  # second half of the message

    rotation1 = 0  # rotation for the first half
    for c in msg1:
        rotation1 += ord(c) - ord('A')
    rotation1 %= 26

    rotation2 = 0  # rotation for the second half
    for c in msg2:
        rotation2 += ord(c) - ord('A')
    rotation2 %= 26

    msg1 = ''.join(chr((ord(c) - ord('A') + rotation1) % 26 + ord('A')) for c in msg1)
    msg2 = ''.join(chr((ord(c) - ord('A') + rotation2) % 26 + ord('A')) for c in msg2)


    return ''.join(chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A')) for c1, c2 in zip(msg1, msg2))  # return the encrypted message

def main():
    msg = input()  # get the message
    print(encrypt(msg))  # print the encrypted message

if __name__ == '__main__':
    main()
