# input
from collections import Counter

inp = input().split()
inp_molecule = Counter(inp[0])
inp_molecule['C'] = inp_molecule.get('C', 0) * int(inp[1])  # multiply the number of C atoms by the number of molecules

out_molecule = Counter(input())  # get the output molecule

# print(inp_molecule)
# print(out_molecule)

# print(inp_molecule.get('C', 0))
# print(out_molecule.get('C', 0))

if inp_molecule.get('C', 0) >= out_molecule.get('C', 0):
    if inp_molecule.get('H', 0) >= out_molecule.get('H', 0):
        print(int(inp_molecule.get('C', 0) / out_molecule.get('C', 0)))
    else:
        print(0)
else:
    print(0)
