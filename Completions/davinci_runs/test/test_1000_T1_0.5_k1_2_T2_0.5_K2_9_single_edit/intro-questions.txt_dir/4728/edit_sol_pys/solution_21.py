
import sys
import re

def parse_molecule(molecule):
    """
    Parse a molecule into a dict of atoms and counts
    """
    atoms = {}
    atom_regex = re.compile(r'([A-Z][a-z]?)(\d*)')
    for atom, count in atom_regex.findall(molecule):
        if count == '':
            count = 1
        else:
            count = int(count)
        atoms[atom] = atoms.get(atom, 0) + count
    return atoms


def main():
    input_molecule, input_count = sys.stdin.readline().strip().split()
    input_count = int(input_count)
    output_molecule = sys.stdin.readline().strip()
    input_atoms = parse_molecule(input_molecule)
    output_atoms = parse_molecule(output_molecule)
    for atom, count in output_atoms.items():
        if atom not in input_atoms or count > input_atoms[atom]:
            print(0)
            return
    output_count = min(input_atoms[atom] // count for atom, count in output_atoms.items())[0]
    print(output_count)


if __name__ == '__main__':
    main()
