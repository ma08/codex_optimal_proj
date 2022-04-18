

def main():
    n, m = map(int, input().split())
    last = input()  # last n-1 characters of the ciphertext
    cipher = input()  # the whole ciphertext
    key = last + cipher[:m-n]  # the key is the last n-1 characters of the ciphertext + the first m-n characters of the ciphertext
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)


if __name__ == "__main__":
    main()
