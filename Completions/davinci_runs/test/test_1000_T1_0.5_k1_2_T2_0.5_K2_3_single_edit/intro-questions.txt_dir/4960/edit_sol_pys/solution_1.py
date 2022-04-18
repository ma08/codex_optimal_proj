
binNumber = input()
octNumber = ''

while len(binNumber) % 3 != 0:
    binNumber = '0' + binNumber

for i in range(0, len(binNumber), 3):
    octNumber += str(int(binNumber[i:i+3], 2))

print(octNumber)

#%%
