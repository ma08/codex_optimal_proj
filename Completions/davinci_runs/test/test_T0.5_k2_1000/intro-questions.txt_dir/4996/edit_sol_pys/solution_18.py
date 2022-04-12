

def main():
    message = input("Enter message: ")
    key = input("Enter key: ")
    encrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            encrypted += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    print(encrypted)

main()
