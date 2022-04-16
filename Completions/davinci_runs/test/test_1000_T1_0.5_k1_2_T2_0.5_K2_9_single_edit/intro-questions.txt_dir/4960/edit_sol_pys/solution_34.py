

bin = input("Enter binary number: ")

n = len(bin)

octal = ""

for i in range(0, n, 4):
    octal += str(int(bin[i:i+4], 2))

print(octal)
