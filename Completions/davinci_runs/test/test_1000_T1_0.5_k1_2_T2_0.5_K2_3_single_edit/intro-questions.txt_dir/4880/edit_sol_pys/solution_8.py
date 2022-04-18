
import sys

    # Reads the input from stdin
def main():
    n, m = map(int, sys.stdin.readline().split())
    keyword = sys.stdin.readline().strip()

    # Decrypts the cipher using the keyword
    cipher = sys.stdin.readline().strip()
    plain = []
    for i in range(1, m):

    # Prints the decrypted message
        plain.append(chr((ord(cipher[i]) - ord(keyword[i])) % 26 + 97))
    print("".join(plain))

if __name__ == "__main__":
    main()
