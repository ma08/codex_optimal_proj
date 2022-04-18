
binary = input()
binary = binary[::-1]
binary = binary + (3 - len(binary) % 3) * '0'
octal = ''
for i in range(0, len(binary), 3):
    octal += str(int(binary[i:i + 3], 2))

print(octal[::-1])
