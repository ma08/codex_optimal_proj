
import string

def main():
    n, m = map(int, input().split()) #n is length of last, m is length of cipher
    last = input()
    cipher = input()
    key = last + cipher[:m-n] #key is the repeated key
    plain = ""
    for i in range(m):
        plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))
    print(plain)

main()
