

def get_molecules(molecule):
    """
    Returns a list of tuples of the form (atom, count).
    """
    molecules = []
    current = ""
    for c in molecule:
        if c.isalpha():
            if current != "":
                molecules.append((current[0], int(current[1:])))
                current = ""
            current += c
        else:
            current += c
    if current != "":
        molecules.append((current[0], int(current[1:])))
    return molecules

def remove_molecules(molecules, molecule):
    """
    Removes the given molecule from the list of molecules.
    Returns a new list of molecules.
    """
    for atom, count in molecule:
        for i, (a, c) in enumerate(molecules):
            if a == atom:
                if c < count:
                    return None
                elif c == count:
                    del molecules[i]
                else:
                    molecules[i] = (a, c - count)
                break
    return molecules

def main():
    input_molecule = input()
    input_count = int(input())
    output_molecule = input()
    input_molecules = get_molecules(input_molecule)
    output_molecules = get_molecules(output_molecule)
    output_count = 0
    while True:
        input_molecules = remove_molecules(input_molecules, output_molecules)
        if input_molecules is None:
            break
        output_count += 1
        if output_count == input_count:
            break
    print(output_count)

main()
