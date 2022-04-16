
import re
from collections import Counter

inp = input().split()
inp_molecule = Counter(re.findall('[A-Z][a-z]?', inp[0]))
inp_molecule['C'] = inp_molecule['C'] * int(inp[1])
out_molecule = Counter(re.findall('[A-Z][a-z]?', input()))

# print(inp_molecule)
# print(out_molecule)

# print(inp_molecule.get('C', 0))
# print(out_molecule.get('C', 0))

if inp_molecule['C'] >= out_molecule['C']:
    if inp_molecule['H'] >= out_molecule['H']:
        print(int(inp_molecule['C'] / out_molecule['C']))
    else:
        print(0)
else:
    print(0)
