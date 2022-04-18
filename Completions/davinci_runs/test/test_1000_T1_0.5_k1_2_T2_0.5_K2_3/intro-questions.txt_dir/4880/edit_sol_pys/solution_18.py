
n, m = map(int, input().split())
key = input()
cipher = input()

plain = ""

# first n letters of plaintext are the same as the key
plain += key

# next m-n letters of plaintext are the ciphertext minus the corresponding letters of the key
for i in range(m-n):
    plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))

print(plain)
