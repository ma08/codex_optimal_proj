
# input
from collections import Counter

inp = input()
inp_molecule = Counter(inp)
inp_molecule['C'] = inp_molecule.get('C', 0) * int(input())

out_molecule = Counter(input())

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
