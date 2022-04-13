

n, m = map(int, input().split())  # n=length of key, m=length of ciphertext
key = input()
cipher = input()

plain = ""

# first n letters of plaintext are the same as the key
plain += key

# next m-n letters of plaintext are the ciphertext minus the corresponding letter of the key mod 26 (add 26 to make sure the subtraction doesn't result in a negative number)
for i in range(m - n):
    plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))

print(plain)
