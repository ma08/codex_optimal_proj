import sys

def parse_molecule(molecule):
    atoms = {}
    s = 0
    while s < len(molecule):
        atom = molecule[s]
        s += 1
        if s < len(molecule) and molecule[s] in '0123456789':
            atoms[atom] = atoms.get(atom, 0) + int(molecule[s])
            s += 1
        else:
            atoms[atom] = atoms.get(atom, 0) + 1
    return atoms

def solve(input_molecule, output_molecule, n):
    input_atoms = parse_molecule(input_molecule * n)
    output_atoms = parse_molecule(output_molecule)
    for atom in output_atoms:
        if atom not in input_atoms or output_atoms[atom] > input_atoms[atom]:
            return 0
    return n

def main():
    input_molecule, n_str = sys.stdin.readline().split()
    n = int(n_str)
    output_molecule = sys.stdin.readline()
    print(solve(input_molecule, output_molecule.strip(), n))

if __name__ == "__main__":
    main()
