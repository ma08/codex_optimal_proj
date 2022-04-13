import sys


def parse_molecule(molecule):
    atoms = {}
    for c in molecule:
        if c.isupper():
            atoms[c] = atoms.get(c, 0) + 1
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
