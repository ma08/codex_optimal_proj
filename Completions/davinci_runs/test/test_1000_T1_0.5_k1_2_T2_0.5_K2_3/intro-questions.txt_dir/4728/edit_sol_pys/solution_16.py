

from collections import defaultdict

inp_molecule = defaultdict(int, {inp[0]: int(inp[1])})

out_molecule = defaultdict(int, {input()[0]: int(input()[1])})


if inp_molecule['C'] >= out_molecule['C']:
    if inp_molecule['H'] >= out_molecule['H']:
        print(int(inp_molecule['C'] / out_molecule['C']))
    else:
        print(0)
else:
    print(0)
