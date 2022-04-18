
 
binary = input()[::-1]

octa = []
for i in range(0, len(binary), 3):
    if i+3 > len(binary):
        octa.append(binary[i:])
    else:
        octa.append(binary[i:i+3])

octa = [str(int(x, 2)) for x in octa]
octa = "".join(octa[::-1])
print(octa)
