

def main():
    message = input()
    key = input()
    encrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted += chr((ord(message[i]) - ord(key[i])) % 26 + ord('A'))
        else:
            encrypted += chr((ord(message[i]) - ord(key[i])) % 26 + ord('A'))
    print(encrypted)

main()
