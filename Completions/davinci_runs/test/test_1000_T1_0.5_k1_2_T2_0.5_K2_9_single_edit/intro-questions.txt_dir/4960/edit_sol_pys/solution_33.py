

bin = input()

n = len(bin)

octal = '0o'

for i in range(0, n, 3):
    octal += str(int(bin[i:i+3], 2))     #convert 3 bits to integer and add it to octal

print(octal)
