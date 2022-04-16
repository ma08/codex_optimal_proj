

def get_molecule(molecule):
    """
    Returns a list of tuples of the form (atom, count)
    """
    molecules = {}
    current = ""
    for c in molecule:
        if c.isalpha():
            if current != "":
                molecules[current[0]] = int(current[1:])
                current = ""
            current += c
        else:
            current += c
    if current != "":
        molecules[current[0]] = int(current[1:])
    return molecules

def remove_molecule(molecules, molecule):
    """
    Removes the given molecule from the list of molecules.
    Returns a new list of molecules.
    """
    for atom, count in molecules.items():
        if atom not in molecule:
            return None
        if count < molecule[atom]:
            return None
        if count == molecule[atom]:
            del molecules[atom]
        else:
            molecules[atom] = count - molecule[atom]
    return molecules

def main():
    input_molecule, input_count = input().split()
    input_count = int(input_count)
    output_molecule = input()
    input_molecules = get_molecule(input_molecule)
    output_molecules = get_molecule(output_molecule)
    output_count = 0
    while True:
        input_molecules = remove_molecule(input_molecules, output_molecules)
        if input_molecules is None:
            break
        output_count += 1
        if output_count == input_count:
            break
    print(output_count)

main()
