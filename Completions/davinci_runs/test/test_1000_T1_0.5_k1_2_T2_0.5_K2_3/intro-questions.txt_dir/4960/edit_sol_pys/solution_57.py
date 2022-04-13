
binary = input()
binary = binary[::-1]
binary = binary + (3 - len(binary) % 3) * '0'  # adds 0's to the end of the binary string
octal = ''
for i in range(0, len(binary), 3):
    octal += str(int(binary[i:i + 3], 2))

print(int(octal[::-1]))  # reverses the octal string

binary = input()
binary = binary[::-1]
binary = binary + (3 - len(binary) % 3) * '0'  # adds 0's to the end of the binary string
octal = ''
for i in range(0, len(binary), 3):
    octal += str(int(binary[i:i + 3], 2))

print(int(octal[::-1]))  # reverses the octal string
