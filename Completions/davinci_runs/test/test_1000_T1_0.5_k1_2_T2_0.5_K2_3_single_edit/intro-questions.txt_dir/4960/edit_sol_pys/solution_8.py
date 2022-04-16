

binary = input()
binary = binary[::-1]
binary = binary + (4 - len(binary) % 4) * '0'
octal = ''
for i in range(0, len(binary), 4):
    octal += str(int(binary[i:i + 4], 2))

print(int(octal[::-1]))
