

binary = input("enter binary: ")
binary = binary[::-1] #reverse the binary
 
octal = []
for i in range(0, len(binary), 3):
    if i+3 > len(binary): #if the length of the binary is not divisible by 3
        octal.append(binary[i:])
    else:
        octal.append(binary[i:i+3])

octal = [str(int(x, 2)) for x in octal]
octal = "".join(octal[::-1])
print(octal)
