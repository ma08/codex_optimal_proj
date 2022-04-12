
import sys

def main():
    n,m = map(int, sys.stdin.readline().split())
    last_n = sys.stdin.readline().strip()  # last n characters of plaintext
    ciphertext = sys.stdin.readline().strip()
    plaintext = ""
    for i in range(m):
        plaintext += chr((ord(ciphertext[i]) - ord(last_n[i]) + 26) % 26 + ord('a'))  # decrypt the current character
        if i >= n - 1:
            last_n += plaintext[i]
    print(plaintext)

if __name__ == '__main__':
    main()
