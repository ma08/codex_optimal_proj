

def get_molecules(input):
    """
    Returns a list of tuples of the form (atom, count)
    """
    molecules = []
    current = ""
    for c in input:
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

def remove_molecules(molecules, output):
    """
    Removes the given molecule from the list of molecules.
    Returns a new list of molecules.
    """
    for atom, count in output:
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
    input, input_count = input().split()
    input_count = int(input_count) # number of times to apply the reaction
    output = input()
    input_molecules = get_molecules(input)
    output_molecules = get_molecules(output)
    output_count = 0 # number of times the reaction has been applied
    while True:
        input_molecules = remove_molecules(input_molecules, output_molecules)
        if input_molecules is None:
            break
        output_count += 1
        if output_count == input_count:
            break
    print(output_count)

main()
