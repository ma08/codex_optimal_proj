import sys


def parse_molecule(molecule):
    atoms = {}
    i = 0
    while i < len(molecule):
        atom = molecule[i]
        if atom.isupper():
            if i + 1 < len(molecule) and molecule[i + 1].islower():
                atom += molecule[i + 1]
                i += 1
            if i + 1 < len(molecule) and molecule[i + 1].isdigit():
                count = 0
                while i + 1 < len(molecule) and molecule[i + 1].isdigit():
                    count = count * 10 + int(molecule[i + 1])
                    i += 1
                atoms[atom] = atoms.get(atom, 0) + count
            else:
                atoms[atom] = atoms.get(atom, 0) + 1
        i += 1
    return atoms



def solve(input_molecule, output_molecule, n):
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    for atom in output_atoms:
        if atom not in input_atoms or output_atoms[atom] > input_atoms[atom] * n:
            return 0
    return n


def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(input_molecule, output_molecule, n))


if __name__ == "__main__":
    main()
