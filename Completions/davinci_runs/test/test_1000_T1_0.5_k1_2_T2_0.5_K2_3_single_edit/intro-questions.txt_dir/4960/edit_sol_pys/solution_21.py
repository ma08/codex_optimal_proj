
bin = input()

n = len(bin)

octal = ""

for i in range(0, n, 3):
    octal += str(int(bin[i:i+3], 2))

print(octal)
