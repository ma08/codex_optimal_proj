

import math

inp = input().split(' ')
inp_molecule = dict()
inp_molecule['C'] = len(inp[0]) * int(inp[1])
inp_molecule['H'] = len(inp[0]) * int(inp[1])
out_molecule = dict()
out_molecule['C'] = len(inp[2])
out_molecule['H'] = len(inp[2])

print(inp_molecule)
print(out_molecule)

if inp_molecule['C'] >= out_molecule['C']:
    if inp_molecule['H'] >= out_molecule['H']:
        print(math.floor(inp_molecule['C'] / out_molecule['C']))
else:
    print(0)

# if inp_molecule.get('C', 0) >= out_molecule.get('C', 0):
#     if inp_molecule.get('H', 0) >= out_molecule.get('H', 0):
#         print(int(inp_molecule.get('C', 0) / out_molecule.get('C', 0)))
#     else:
#         print(0)
# else:
#     print(0)
