

def get_molecule(molecule_string):
    """
    Returns a list of tuples of the form (element, count)
    """
    molecule = []
    current = ""
    for c in molecule_string:
        if c.isalpha():
            if current != "":
                molecule.append((current[0], int(current[1:])))
                current = ""
            current += c
        else:
            current += c
    if current != "":
        molecule.append((current[0], int(current[1:])))
    return molecule

def remove_molecule(molecules, molecule):
    """
    Removes the given molecule from the list of molecule.
    Returns a new list of molecules.
    """
    for element, count in molecule:
        for i, (e, c) in enumerate(molecules):
            if e == element:
                if c < count:
                    return None
                elif c == count:
                    del molecules[i]
                else:
                    molecules[i] = (e, c - count)
                break
    return molecules

def main():
    input_molecule, input_count = input().split()
    input_count = int(input_count)
    output_molecule = input()
    input_molecule = get_molecule(input_molecule)
    output_molecule = get_molecule(output_molecule)
    output_count = 0
    while True:
        input_molecule = remove_molecule(input_molecule, output_molecule)
        if input_molecule is None:
            break
        output_count += 1
        if output_count == input_count:
            break
    print(output_count)

main()
