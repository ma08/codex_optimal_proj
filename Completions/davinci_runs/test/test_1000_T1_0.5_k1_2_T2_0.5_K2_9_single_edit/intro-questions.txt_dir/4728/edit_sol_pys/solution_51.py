

import sys

# # File I/O
# in_file = open('Cesium.txt', 'r')
# sys.stdin = in_file

# Read input
input_string = input().split()
input_molecule = input_string[0]
input_count = int(input_string[1])
output_molecule = input()

# Determine input molecule atoms
input_atoms = []
curr_atom = ''
for character in input_molecule:
    if character.isalpha():
        if curr_atom != '':
            input_atoms.append(curr_atom)
        curr_atom = character
    else:
        curr_atom += character
input_atoms.append(curr_atom)

# Determine output molecule atoms
output_atoms = []
curr_atom = ''
for character in output_molecule:
    if character.isalpha():
        if curr_atom != '':
            output_atoms.append(curr_atom)
        curr_atom = character
    else:
        curr_atom += character
output_atoms.append(curr_atom)

# Determine input atom counts
input_atom_counts = {}
for atom in input_atoms:
    if atom[0] in input_atom_counts:
        input_atom_counts[atom[0]] += int(atom[1:])
    else:
        input_atom_counts[atom[0]] = int(atom[1:])

# Determine output atom counts
output_atom_counts = {}
for atom in output_atoms:
    if atom[0] in output_atom_counts:
        output_atom_counts[atom[0]] += int(atom[1:])
    else:
        output_atom_counts[atom[0]] = int(atom[1:])

# Determine output count
output_count = 0
for atom in output_atom_counts:
    if atom in input_atom_counts:
        output_count = max(output_count, input_atom_counts[atom] // output_atom_counts[atom])

# Output result
print(output_count * input_count)
