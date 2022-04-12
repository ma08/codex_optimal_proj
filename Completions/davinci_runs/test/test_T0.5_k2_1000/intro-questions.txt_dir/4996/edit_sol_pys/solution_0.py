

def encrypt(c, k):
    encrypted = ""
    for i in range(len(c)):
        if i % 2 == 0:
            encrypted += chr((ord(c[i]) - ord(k[i]) + 26) % 26 + ord('A'))
        else:
            encrypted += chr((ord(c[i]) - ord(k[i]) - 26) % 26 + ord('A'))
    return encrypted

print(encrypt(input(), input()))
