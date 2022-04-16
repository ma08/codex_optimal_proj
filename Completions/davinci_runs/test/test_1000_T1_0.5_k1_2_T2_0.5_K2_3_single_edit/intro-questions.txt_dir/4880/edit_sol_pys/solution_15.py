

import sys

def main():
    n, m = map(int, sys.stdin.readline().split()) # n = last n characters
    lastn = sys.stdin.readline().strip() # last n characters
    ciphertext = sys.stdin.readline().strip() # ciphertext
    prefix = lastn[-n:]
    plaintext = "" # plaintext
    for i in range(m):
        c = ciphertext[i]
        if i < n:
            p = prefix[i]
        else:
            p = plaintext[i-n] # previous n characters
        plaintext += chr((ord(c) - ord(p) + 26) % 26 + ord('a'))
    print(plaintext)

if __name__ == "__main__":
    main()
