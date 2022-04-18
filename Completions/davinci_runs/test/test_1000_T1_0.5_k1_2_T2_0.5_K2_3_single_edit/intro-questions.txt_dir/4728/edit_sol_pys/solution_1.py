import sys
import math

def solve(n, input_molecule, output_molecule):
    if len(input_molecule) % len(output_molecule) != 0:
        return 0
    output_molecule_count = len(input_molecule) // len(output_molecule)
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    for atom in output_atoms:
        if atom not in input_atoms or output_atoms[atom] > input_atoms[atom] * n:
            return 0
    return math.factorial(output_molecule_count)


def parse_molecule(molecule):
    atoms = {}
    s = 0
    while s < len(molecule):
        atom = molecule[s]
        s += 1
        if s < len(molecule) and molecule[s].isdigit():
            atoms[atom] = atoms.get(atom, 0) + int(molecule[s])
            s += 1
        else:
            atoms[atom] = atoms.get(atom, 0) + 1
    return atoms

def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(n, input_molecule, output_molecule))

if __name__ == "__main__":
    main()
