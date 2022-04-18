import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    last = sys.stdin.readline()
    cipher = sys.stdin.readline()
    key = last + cipher[:m-n]
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)

main()
