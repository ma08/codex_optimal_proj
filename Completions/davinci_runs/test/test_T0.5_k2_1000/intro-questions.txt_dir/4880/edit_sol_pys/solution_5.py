
n, m = map(int, input().split())
key = input()
cipher = input()

plain = ""

# first n letters of plaintext are the same as the key
plain += key

# next m-n letters of plaintext are the ciphertext minus the corresponding letter of the key, mod 26
for i in range(n, m):
    plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a'))

print(plain)
