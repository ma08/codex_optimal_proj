

def main():
    message = input()
    key = input()
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            decrypted += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('A'))
    print(decrypted)

main()