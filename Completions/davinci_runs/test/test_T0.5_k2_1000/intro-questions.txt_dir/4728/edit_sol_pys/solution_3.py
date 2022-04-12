

import re
import sys

# Check for a single element
def check_single(input, output):
    """
    Checks if a single element is present in the input and output.
    """
    input_elements = set(re.findall(r'\w', input))
    output_elements = set(re.findall(r'\w', output))
    if len(input_elements) == 1 and len(output_elements) == 1:
        return True
    else:
        return False

# Check if elements are the same
def check_elements(input, output):
    """
    Checks if the elements in the input and output are the same.
    """
    input_elements = set(re.findall(r'\w', input))
    output_elements = set(re.findall(r'\w', output))
    if input_elements == output_elements:
        return True
    else:
        return False

# Check if input and output are the same
def check_same(input, output):
    """
    Checks if the input and output are the same.
    """
    if input == output:
        return True
    else:
        return False

# Count the number of elements in the input
def count_input_elements(input):
    """
    Counts the number of elements in the input.
    """
    input_elements = {}
    for element in re.findall(r'\w', input):
        if element not in input_elements:
            input_elements[element] = 1
        else:
            input_elements[element] += 1
    return input_elements

# Count the number of elements in the output
def count_output_elements(output):
    """
    Counts the number of elements in the output.
    """
    output_elements = {}
    for element in re.findall(r'\w', output):
        if element not in output_elements:
            output_elements[element] = 1
        else:
            output_elements[element] += 1
    return output_elements

# Count the number of atoms in the input
def count_input_atoms(input):
    """
    Counts the number of atoms in the input.
    """
    input_atoms = {}
    for element in re.findall(r'\w\d*', input):
        if element[0] not in input_atoms:
            if len(element) == 1:
                input_atoms[element[0]] = 1
            else:
                input_atoms[element[0]] = int(element[1:])
        else:
            if len(element) == 1:
                input_atoms[element[0]] += 1
            else:
                input_atoms[element[0]] += int(element[1:])
    return input_atoms

# Count the number of atoms in the output
def count_output_atoms(output):
    """
    Counts the number of atoms in the output.
    """
    output_atoms = {}
    for element in re.findall(r'\w\d*', output):
        if element[0] not in output_atoms:
            if len(element) == 1:
                output_atoms[element[0]] = 1
            else:
                output_atoms[element[0]] = int(element[1:])
        else:
            if len(element) == 1:
                output_atoms[element[0]] += 1
            else:
                output_atoms[element[0]] += int(element[1:])
    return output_atoms

# Calculate the number of output molecules
def calc_output_molecules(input_atoms, output_atoms):
    """
    Calculates the number of output molecules.
    """
    output_molecules = 0
    for element in output_atoms:
        if element in input_atoms:
            output_molecules += input_atoms[element] / output_atoms[element]
        else:
            output_molecules = 0
            break
    return output_molecules

# Calculate the number of output molecules 2
def calc_output_molecules_2(input_atoms, output_atoms):
    """
    Calculates the number of output molecules.
    """
    output_molecules = 0
    for element in output_atoms:
        if element in input_atoms:
            output_molecules += input_atoms[element] / output_atoms[element]
        else:
            output_molecules = 0
            break
    return output_molecules

# Main function
def main():
    """
    Main function.
    """
    input_line = sys.stdin.readline()
    input_line = input_line.rstrip()
    input = input_line.split(' ')
    input_molecule = input[0]
    input_molecules = int(input[1])

    output_molecule = sys.stdin.readline()
    output_molecule = output_molecule.rstrip()

    # Check for a single element
    if check_single(input_molecule, output_molecule):
        print 0
        return

    # Check if elements are the same
    if check_elements(input_molecule, output_molecule):
        # Check if input and output are the same
        if check_same(input_molecule, output_molecule):
            print input_molecules
            return
        else:
            # Count the number of atoms in the input
            input_atoms = count_input_atoms(input_molecule)
            # Count the number of atoms in the output
            output_atoms = count_output_atoms(output_molecule)
            # Calculate the number of output molecules
            output_molecules = calc_output_molecules(input_atoms, output_atoms)
            print int(output_molecules)
            return

    # Count the number of elements in the input
    input_elements = count_input_elements(input_molecule)
    # Count the number of elements in the output
    output_elements = count_output_elements(output_molecule)

    # Count the number of atoms in the input
    input_atoms = count_input_atoms(input_molecule)
    # Count the number of atoms in the output
    output_atoms = count_output_atoms(output_molecule)

    # Calculate the number of output molecules
    output_molecules = calc_output_molecules(input_atoms, output_atoms)

    # Calculate the number of output molecules
    output_molecules_2 = calc_output_molecules_2(input_elements, output_elements)

    if output_molecules_2 == 0:
        print 0
    else:
        print int(min(output_molecules, output_molecules_2))

# Run main function
if __name__ == '__main__':
    main()
