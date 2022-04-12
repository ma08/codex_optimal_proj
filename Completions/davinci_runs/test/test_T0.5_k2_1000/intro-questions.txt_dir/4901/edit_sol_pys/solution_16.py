
def main():
    message = input()
    left = message[:len(message)//2]
    right = message[len(message)//2:]
    left_rotate = sum([(ord(char) - ord('A')) for char in left]) % 26
    right_rotate = sum([(ord(char) - ord('A')) for char in right]) % 26

    decrypted = ''
    for i in range(len(left)):
        left_char = (ord(left[i]) - ord('A') - left_rotate) % 26
        right_char = (ord(right[i]) - ord('A') - right_rotate) % 26
        decrypted += chr(((left_char + right_char) % 26) + ord('A'))

    print(decrypted)

if __name__ == '__main__':
    main()
