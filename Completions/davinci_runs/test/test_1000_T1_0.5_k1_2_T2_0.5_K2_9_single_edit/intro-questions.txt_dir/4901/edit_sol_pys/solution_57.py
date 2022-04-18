

def main():
    message = input()
    left = message[:len(message)//2]
    right = message[len(message)//2:]
    left_rotate = sum([(ord(char) - ord('A') + 1) for char in left])
    right_rotate = sum([(ord(char) - ord('A') + 1) for char in right])

    decrypted = ''
    for i in range(len(left)):
        left_char = ord(left[i]) - ord('A') + 1
        right_char = ord(right[i]) - ord('A') + 1
        decrypted += chr(((left_char + right_char + right_rotate) % 26) + ord('A') - 1)

    print(decrypted)

if __name__ == '__main__':
    main()
