import sys

def main():
    message = sys.stdin.readline().strip()
    key = sys.stdin.readline().strip()
    decrypted = ""
    for i in range(len(message)):
        if i % 2 == 0:
            decrypted += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted += chr((ord(message[i]) - ord(key[i]) - 26) % 26 + ord('a'))
    print(decrypted)

main()
