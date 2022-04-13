
import sys

in_file = open('Cesium.txt', 'r')
sys.stdin = in_file

input_string = input().split()
input_molecule = input_string[0]
input_count = int(input_string[1])
output_molecule = input()

input_atom_counts = {}
curr_atom = input_molecule[0]
for i in range(1, len(input_molecule)):
    if input_molecule[i].isalpha():
        if curr_atom[0] in input_atom_counts:
            input_atom_counts[curr_atom[0]] += int(curr_atom[1:])
        else:
            input_atom_counts[curr_atom[0]] = int(curr_atom[1:])
        curr_atom = input_molecule[i]
    else:
        curr_atom += input_molecule[i]
if curr_atom[0] in input_atom_counts:
    input_atom_counts[curr_atom[0]] += int(curr_atom[1:])
else:
    input_atom_counts[curr_atom[0]] = int(curr_atom[1:])

output_atom_counts = {}
curr_atom = output_molecule[0]
for i in range(1, len(output_molecule)):
    if output_molecule[i].isalpha():
        if curr_atom[0] in output_atom_counts:
            output_atom_counts[curr_atom[0]] += int(curr_atom[1:])
        else:
            output_atom_counts[curr_atom[0]] = int(curr_atom[1:])
        curr_atom = output_molecule[i]
    else:
        curr_atom += output_molecule[i]
if curr_atom[0] in output_atom_counts:
    output_atom_counts[curr_atom[0]] += int(curr_atom[1:])
else:
    output_atom_counts[curr_atom[0]] = int(curr_atom[1:])

output_count = 0
for atom in output_atom_counts:
    if atom in input_atom_counts:
        output_count = max(output_count, input_atom_counts[atom] // output_atom_counts[atom])

print(output_count * input_count)
