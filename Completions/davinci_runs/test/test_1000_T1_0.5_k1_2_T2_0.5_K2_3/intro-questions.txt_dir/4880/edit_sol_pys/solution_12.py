

import sys

def main():
    n,m = map(int, sys.stdin.readline().split())
    last_n = sys.stdin.readline().strip()[-n:]
    cipher = sys.stdin.readline().strip()
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(last_n[i % n]) + 26) % 26 + ord('a'))
        if i >= n - 1:
            last_n += plain[i]
    print(plain)

if __name__ == '__main__':
    main()
