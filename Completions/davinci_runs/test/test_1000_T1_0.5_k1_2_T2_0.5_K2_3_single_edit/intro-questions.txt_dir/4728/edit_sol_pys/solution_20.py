

def parse_molecule(mol):
    """
    Parses a molecule string into a dictionary of atoms and their counts.

    :param mol: The molecule string to parse.
    :return: A dictionary of atoms and their counts.
    """
    atoms = {}

    # Keep track of the current atom and count
    current_atom = ''
    current_count = 0

    for c in mol:
        if c.isalpha():
            # If we have a current atom, save it
            if current_atom:
                atoms[current_atom] = current_count  # noqa

            # Start a new atom
            current_atom = c
            current_count = 0
        else:
            # If we have a current atom, add this digit to its count
            if current_atom:
                current_count = current_count * 10 + int(c)  # noqa
            else:
                # We have a digit but no atom, so this is an error
                raise Exception('Invalid molecule string: ' + mol)

    # Save the last atom
    if current_atom:
        atoms[current_atom] = current_count

    return atoms


def count_atoms(mol):
    """
    Counts the total number of atoms in a molecule.

    :param mol: The molecule string to count.
    :return: The total number of atoms in the molecule.
    """
    atoms = parse_molecule(mol)

    total = 0
    for count in atoms.values():
        total += count

    return total


def combine_atoms(atoms1, atoms2):
    """
    Combines two dictionaries of atoms and counts.

    :param atoms1: The first dictionary of atoms and counts.
    :param atoms2: The second dictionary of atoms and counts.
    :return: A dictionary of all atoms and their combined counts.
    """
    combined = {}

    for atom in atoms1:
        combined[atom] = atoms1[atom]

    for atom in atoms2:
        if atom in combined:
            combined[atom] += atoms2[atom]
        else:
            combined[atom] = atoms2[atom]

    return combined


def subtract_atoms(atoms1, atoms2):
    """
    Subtracts the second atom dictionary from the first.

    :param atoms1: The first dictionary of atoms and counts.
    :param atoms2: The second dictionary of atoms and counts.
    :return: A dictionary of all atoms and their counts after subtracting the second from the first.
    """
    subtracted = {}

    for atom in atoms1:
        subtracted[atom] = atoms1[atom]

    for atom in atoms2:
        if atom in subtracted:
            subtracted[atom] -= atoms2[atom]
        else:
            subtracted[atom] = -atoms2[atom]

    return subtracted


def has_negative_atoms(atoms):
    """
    Checks if a dictionary of atoms and counts has any negative counts.

    :param atoms: The dictionary of atoms and counts to check.
    :return: True if the dictionary contains any negative counts, false otherwise.
    """
    for count in atoms.values():
        if count < 0:
            return True

    return False


def run_reaction(mol, reaction):
    """
    Runs a reaction on a molecule.

    :param mol: The molecule to run the reaction on.
    :param reaction: The reaction to run.
    :return: The molecule after the reaction has been run.
    """
    input_atoms = parse_molecule(mol)
    output_atoms = parse_molecule(reaction)

    # Subtract the output atoms from the input atoms
    subtracted_atoms = subtract_atoms(input_atoms, output_atoms)

    # If any atoms have negative counts, the reaction is impossible
    if has_negative_atoms(subtracted_atoms):
        return mol

    # Add the remaining atoms to the output atoms
    combined_atoms = combine_atoms(output_atoms, subtracted_atoms)

    # Convert the atoms back to a molecule string
    new_mol = ''
    for atom in combined_atoms:
        new_mol += atom
        if combined_atoms[atom] != 1:
            new_mol += str(combined_atoms[atom])  # noqa

    return new_mol


def react(mol, reactions):
    """
    Runs a list of reactions on a molecule.

    :param mol: The molecule to run the reactions on.
    :param reactions: A list of reactions to run.
    :return: The molecule after the reactions have been run.
    """
    for reaction in reactions:
        mol = run_reaction(mol, reaction)

    return mol


def main():
    # Get the input molecule and number of molecules
    input_mol, input_count = input().split()
    input_count = int(input_count)

    # Get the output molecule
    output_mol = input()

    # Get the number of reactions
    num_reactions = int(input())

    # Get the reactions
    reactions = []
    for i in range(num_reactions):
        reactions.append(input())

    # Run the reactions on the input molecule
    mol = react(input_mol, reactions)

    # If the input molecule is not the same as the output molecule, the reaction is impossible
    if mol != output_mol:
        print(0)
        return

    # Count the number of atoms in the output molecule
    output_atoms = count_atoms(output_mol)

    # Count the number of atoms in the input molecule
    input_atoms = count_atoms(input_mol)

    # Divide the number of input atoms by the number of output atoms
    num_output = input_atoms // output_atoms

    print(num_output)


if __name__ == '__main__':
    main()
