

bin = input("Enter binary number: ")

n = len(bin)

octal = 0

for i in range(0, n, 3):
    octal += int(bin[i:i+3], 2) * (10 ** (n - i - 3))

print(octal)
