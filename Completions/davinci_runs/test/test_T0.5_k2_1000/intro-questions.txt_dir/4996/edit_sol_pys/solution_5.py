

def main():
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    print("Decrypted message: " + decrypted)

main()
