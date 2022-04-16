

def main():
    n, m = map(int, input().split())
    last = input()
    cipher = input()
    key = last + cipher[:m - n]
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)

main()
