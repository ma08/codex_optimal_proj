
n, m, key, cipher = map(str, input().split())
n, m = int(n), int(m)

plain = ""

# first n letters of plaintext are the same as the key
plain += key

# next m-n letters of plaintext are the ciphertext minus the corresponding letter of the key
for i in range(m-n):
    plain += chr((ord(cipher[i]) - ord(key[i]) + 26) % 26 + ord('a') - 1)

print(plain)
