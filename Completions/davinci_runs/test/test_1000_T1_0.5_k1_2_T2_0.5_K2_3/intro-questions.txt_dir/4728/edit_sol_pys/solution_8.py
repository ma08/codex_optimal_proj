import sys


def solve(input_molecule, output_molecule, n):
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    for atom in output_atoms:
        if atom not in input_atoms or output_atoms[atom] > input_atoms[atom] * n:
            return 0
    
def parse_molecule(molecule):
    atoms = {}
    current_atom = ""
    current_atom_count = 1
    in_brackets = False
    in_brackets_count = 0
    for c in molecule:
        if c.isupper():
            if current_atom:
                atoms[current_atom] = current_atom_count
            current_atom = c
            current_atom_count = 1
        elif c.islower():
            current_atom += c
        elif c.isdigit():
            if in_brackets:
                in_brackets_count = in_brackets_count * 10 + int(c)
            else:
                current_atom_count = current_atom_count * 10 + int(c)
        elif c == '(':
            in_brackets = True
            in_brackets_count = 0
        elif c == ')':
            in_brackets = False
            current_atom_count *= in_brackets_count
    if current_atom:
        atoms[current_atom] = current_atom_count
    return atoms
    return n

def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(input_molecule, output_molecule, n))

if __name__ == "__main__":
    main()
