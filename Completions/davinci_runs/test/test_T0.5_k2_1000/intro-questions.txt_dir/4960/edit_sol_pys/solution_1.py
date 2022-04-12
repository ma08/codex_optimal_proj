

binary = input() #get binary number
binary = binary[::-1] #reverse binary number
binary = binary + (3 - len(binary) % 3) * '0' #add 0 to the end of the binary number
octal = '' #create octal number
for i in range(0, len(binary), 3): #convert binary number to the octal number
    octal += str(int(binary[i:i + 3], 2)) #convert binary number to the octal number

print(int(octal[::-1]))
