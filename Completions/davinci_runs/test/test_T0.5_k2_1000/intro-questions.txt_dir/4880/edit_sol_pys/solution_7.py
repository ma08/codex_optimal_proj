

def main():
    n, m = map(int, input().split()) # n = key length, m = cipher length
    last = input().strip()
    cipher = input().strip()
    key = last + cipher[:m-n-1] # key = last n-1 letters of cipher
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)

main()
