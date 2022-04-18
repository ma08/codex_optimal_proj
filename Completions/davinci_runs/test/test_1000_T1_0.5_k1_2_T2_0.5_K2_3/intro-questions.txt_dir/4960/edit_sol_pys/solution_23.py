bit = input()

n = len(bit)

octal = ""

for i in range(0, n, 3):
    octal += str(int(bit[i:i+3], 2))

print(octal)
