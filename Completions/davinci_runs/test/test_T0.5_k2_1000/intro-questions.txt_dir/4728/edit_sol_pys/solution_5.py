import sys

def parse_molecule(molecule): # parse molecule into a dictionary
    atoms = {}
    s = 0
    while s < len(molecule):
        atom = molecule[s]
        s += 1
        if s < len(molecule) and molecule[s].isdigit(): # if the next character is a number
            atoms[atom] = atoms.get(atom, 0) + int(molecule[s])
            s += 1
        else: # if the next character is not a number
            atoms[atom] = atoms.get(atom, 0) + 1
    return atoms

def solve(input_molecule, output_molecule, n): # find the max number of molecules that can be made
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    for atom in output_atoms: # iterate through atoms in output molecule
        if atom not in input_atoms or output_atoms[atom] > input_atoms[atom] * n:
            return 0 # if the atom is not in the input molecule or the number of atoms in the output molecule is greater than the number of atoms in the input molecule, return 0
    return n

def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(input_molecule, output_molecule, n))

if __name__ == "__main__":
    main()
