
import sys
def main():
    n,m = map(int, sys.stdin.readline().split())
    last_m = sys.stdin.readline().strip()
    ciphertext = sys.stdin.readline().strip()
    plaintext = ""
    for i in range(m):
        plaintext += chr((ord(ciphertext[i]) - ord(last_m[i]) + 26) % 26 + ord('a'))
        if i >= n - 1:
            last_m += plaintext[i]
    print(plaintext)

if __name__ == '__main__':
    main()
