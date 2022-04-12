
def main():
    n, m = map(int, input().split())
    first = input()
    cipher = input()
    key = first + cipher[:m - n]
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)


main()
