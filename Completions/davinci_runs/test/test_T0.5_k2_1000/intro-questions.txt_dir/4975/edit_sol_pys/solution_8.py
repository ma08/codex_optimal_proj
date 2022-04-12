

# Generate the key table.
def key(phrase):
    key = [[], [], [], [], []]
    phrase = [x for x in phrase if x != ' ']
    for i in range(len(phrase)):
        if phrase[i] not in key[i // 5]:
            key[i // 5] += [phrase[i]]
    for j in range(ord('a'), ord('z') + 1):
        if chr(j) not in phrase and chr(j) != 'q':
            for k in range(5):
                if len(key[k]) < 5:
                    key[k] += [chr(j)]
                    break
    return key

#Encrypt the message.
def encrypt(message, key):
    message = [x for x in message if x!=' ']
    for i in range(len(message)):
        if message[i]=='x' and i!=len(message)-1 and message[i+1]=='x':
            message[i] = 'z'
    if len(message)%2!=0:
        message += ['x']
    encrypted = ''
    for i in range(0,len(message),2):
        if message[i]==message[i+1]:
            message.insert(i+1,'x')
        for j in range(5):
            if message[i] in key[j]:
                row1 = j
                col1 = key[j].index(message[i])
            if message[i+1] in key[j]:
                row2 = j
                col2 = key[j].index(message[i+1])
        if row1==row2:
            encrypted += key[row1][(col1+1)%5]
            encrypted += key[row2][(col2+1)%5]
        elif col1==col2:
            encrypted += key[(row1+1)%5][col1]
            encrypted += key[(row2+1)%5][col2]
        else:
            encrypted += key[row1][col2]
            encrypted += key[row2][col1]
    return encrypted.upper()

#Main Program.
phrase = input()
message = input()
print(encrypt(message, key(phrase)))
