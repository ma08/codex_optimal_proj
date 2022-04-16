

def main():
    message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted += chr((ord(message[i]) - ord(key[i % len(key)]) + 26) % 26 + ord('A'))
        else:
            decrypted += chr((ord(message[i]) - ord(key[i % len(key)]) - 26) % 26 + ord('A'))
    print(decrypted)

main()
