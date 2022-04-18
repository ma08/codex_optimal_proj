

def get_molecule(m):
    """
    Returns a list of tuples of the form (element, count)
    """
    molecule = []
    current = ""
    for c in m:
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
    m, c = input().split()
    c = int(c)
    o = input()
    m = get_molecule(m)
    o = get_molecule(o)
    oc = 0
    while True:
        m = remove_molecule(m, o)
        if m is None:
            break
        oc += 1
        if oc == c:
            break
    print(oc)

main()
