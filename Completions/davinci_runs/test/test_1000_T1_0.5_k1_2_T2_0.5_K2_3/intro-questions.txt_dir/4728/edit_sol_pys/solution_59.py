

from collections import defaultdict

inp = input()
inp_molecule = defaultdict(int)
inp_molecule[inp[0]] = float(inp[1])

out_molecule = defaultdict(int)
out_molecule[input()[0]] = float(input()[1])

# print(inp_molecule)
# print(out_molecule)

# print(inp_molecule.get('C', 0))
# print(out_molecule.get('C', 0))

if inp_molecule['C'] >= out_molecule['C']:
    if inp_molecule['H'] >= out_molecule['H']:
        print(round(inp_molecule['C'] / out_molecule['C']))
    else:
        print(0)
else:
    print(0)
