
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    lastn = sys.stdin.readline().strip()
    ciphertext = sys.stdin.readline().strip()
    prefix = lastn[-n:]
    plaintext = ""
    for i in range(m):
        c = ciphertext[i]
        if i < n:
            p = prefix[i]
        else:
            p = plaintext[i-n]
        plaintext += chr((ord(c) - ord(p) + 26) % 26 + ord('a'))
    print(plaintext)

if __name__ == "__main__":
    main()
