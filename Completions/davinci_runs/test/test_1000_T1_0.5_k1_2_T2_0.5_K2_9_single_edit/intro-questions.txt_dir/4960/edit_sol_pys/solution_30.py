

binary = input()
binary = binary[::-1]
print(binary)
octal = []
for i in range(0, len(binary), 3): 
    octal.append(binary[i:i+3])

octal = [str(int(x, 2)) for x in octal]
octal = "".join(octal[::-1])
print(octal)
