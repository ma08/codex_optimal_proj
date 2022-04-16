
from collections import Counter

inp = input().split()
inp_molecule = Counter(inp[0])
inp_molecule['C'] = inp_molecule.get('C', 0) * int(inp[1])

out_molecule = Counter(input())

print(inp_molecule.get('C', 0) / out_molecule.get('C', 0)
      if inp_molecule.get('C', 0) >= out_molecule.get('C', 0)
      else 0)
