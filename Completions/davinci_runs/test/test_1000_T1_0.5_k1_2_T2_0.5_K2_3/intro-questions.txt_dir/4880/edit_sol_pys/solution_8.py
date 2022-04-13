
import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    keyword = sys.stdin.readline().strip()
    cipher = sys.stdin.readline().strip()
    plain = []
    for i in range(0, m):
        plain.append(chr((ord(cipher[i]) - ord(keyword[i % m])) % 26 + 97))
    print("".join(plain))

if __name__ == "__main__":
    main()
