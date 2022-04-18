binary = input()
n = len(binary)
octal = ""

for i in range(0, n, 3):
    octal += str(int(binary[i:i+3], 2))
print(octal)
