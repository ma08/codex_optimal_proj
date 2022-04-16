import sys
import collections

def parse_molecule(molecule):
    atoms = collections.Counter()
    s = 0
    while s < len(molecule):
        atom = molecule[s]
        s += 1
        if s < len(molecule) and molecule[s].isdigit():
            atoms[atom] += int(molecule[s])
            s += 1
        else:
            atoms[atom] += 1
    return atoms

def solve(atoms, output_molecule, n):
    output_atoms = parse_molecule(output_molecule)    
    for atom in output_atoms:
        if atom not in atoms or output_atoms[atom] > atoms[atom] * n:
            return 0
    return n

def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(parse_molecule(input_molecule), output_molecule, n))

if __name__ == "__main__":
    main()
