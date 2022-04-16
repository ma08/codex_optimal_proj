

def decrypt(message, key):
    message = message.upper()
    key = key.upper()
    decrypted_message = ""
    for i in range(len(message)): 
        x = (ord(message[i]) - ord(key[i])) % 26
        x += 65
        decrypted_message += chr(x) 
    return decrypted_message

print(decrypt(input(), input()))
