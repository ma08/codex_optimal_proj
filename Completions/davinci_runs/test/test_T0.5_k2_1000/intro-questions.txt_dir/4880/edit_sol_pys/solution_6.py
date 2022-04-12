
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    key = sys.stdin.readline().strip()
    cipher = sys.stdin.readline().strip()
    plain = []
    for i in range(m):
        plain.append(chr((ord(cipher[i]) - ord(key[i])) % 26 + 97))
    print("".join(plain))

if __name__ == "__main__":
    main()
