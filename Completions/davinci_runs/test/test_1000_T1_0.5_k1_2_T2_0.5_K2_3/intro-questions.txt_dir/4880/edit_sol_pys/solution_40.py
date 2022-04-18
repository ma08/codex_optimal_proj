def main():
    n, m = map(int, input().split()) # n is the length of the key, m is the length of the ciphertext
    key = input() # the key
    cipher = input() # the ciphertext
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i % n]) + 26) % 26 + ord('a'))
    print(plain)


def main():
    n, m = map(int, input().split())
    last = input() # last n-1 characters of the ciphertext
    cipher = input() # the whole ciphertext
    key = last + cipher[:m-n] # the key is the last n-1 characters of the ciphertext + the first m-n characters of the ciphertext
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)

main()
