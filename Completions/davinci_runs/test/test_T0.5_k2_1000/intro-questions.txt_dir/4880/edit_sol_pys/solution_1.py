

def main():
    n, m = map(int, input().split())
    last = input().strip()
    cipher = input().strip()
    key = last + cipher[:m - n - 1]
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)


main()
