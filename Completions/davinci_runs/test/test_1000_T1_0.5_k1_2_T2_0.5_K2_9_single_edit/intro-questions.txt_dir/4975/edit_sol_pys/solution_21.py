

#Generate the key table
def key(phrase):
    key = []
    phrase = phrase.split()
    for i in range(len(phrase)):
        for j in range(len(phrase[i])):
            if phrase[i][j] not in key:
                key += phrase[i][j]
    for j in range(ord('a'), ord('z')+1): 
        if chr(j) not in key and chr(j)!='q':
            key += chr(j)
    key = [key[i:i+5] for i in range(0,len(key),5)]
    return key

#Encrypt the message
def encrypt(message, key):
    message = message.split()
    for i in range(len(message)):
        for j in range(len(message[i])):
            if message[i][j]=='x' and j!=len(message[i])-1 and message[i][j+1]=='x':
                message[i][j] = 'z'
        message[i] = ''.join(message[i])
    message = ''.join(message)
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

#Main Program
phrase = input('Enter the phrase: ')
message = input('Enter the message: ')
print(encrypt(message.lower(), key(phrase.lower())))
