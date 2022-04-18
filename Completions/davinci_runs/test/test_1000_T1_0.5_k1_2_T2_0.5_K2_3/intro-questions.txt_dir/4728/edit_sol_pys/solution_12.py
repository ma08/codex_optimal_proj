

def get_atoms(molecule):
    """
    Returns a list of tuples of the form (atom, number)
    """
    atoms = []
    current = ""
    for c in molecule:
        if c.isalpha():
            if current != "":
                atoms.append((current[0], int(current[1:])))
                current = ""
            current += c
        else:
            current += c
    if current != "":
        atoms.append((current[0], int(current[1:])))
    return atoms

def remove_atoms(atoms, molecule):
    """
    Removes the given molecule from the list of atoms.
    Returns a new list of atoms.
    """
    for atom, number in molecule:
        for i, (a, c) in enumerate(atoms):
            if a == atom:
                if c < number:
                    return None
                elif c == number:
                    del atoms[i]
                else:
                    atoms[i] = (a, c - number)
                break
    return atoms

def main():
    input_molecule, input_count = raw_input().split()
    input_count = int(input_count)
    output_molecule = raw_input()
    input_atoms = get_atoms(input_molecule)
    output_atoms = get_atoms(output_molecule)
    output_count = 0
    while True:
        input_atoms = remove_atoms(input_atoms, output_atoms)
        if input_atoms is None:
            break
        output_count += 1
        if output_count == input_count:
            break
    print(output_count)

main()
