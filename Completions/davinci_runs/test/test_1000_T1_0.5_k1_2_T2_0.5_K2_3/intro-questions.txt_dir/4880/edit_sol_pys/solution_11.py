import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    keyword = sys.stdin.readline().strip()
    ciphertext = sys.stdin.readline().strip()
    plain = []
    for i in range(1, m):
        plain.append(chr((ord(ciphertext[i]) - ord(keyword[i])) % 26 + 97))
    print("".join(plain))

if __name__ == "__main__":
    main()
