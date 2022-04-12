

import sys

def get_input(f):
    """
    Parse the input text file.
    Arguments:
        f: input file
    Returns:
        n: number of DNA samples
        k: length of DNA samples
        dna: list of strings representing the DNA samples
    """
    # Get the first line
    line = f.readline()
    try:
        n, k = map(int, line.split())
    except ValueError:
        print("Invalid Input")
        sys.exit()

    # Get the rest of the lines
    dna = []
    for i in range(n):
        line = f.readline()
        dna.append(line.strip())

    return n, k, dna

def min_unlikeness(n, k, dna):
    """
    Compute the minimal unlikeness of the evolutionary tree.
    Arguments:
        n: number of DNA samples
        k: length of DNA samples
        dna: list of strings representing the DNA samples
    Returns:
        unlikeness: the minimal unlikeness of the evolutionary tree
    """
    unlikeness = 0
    for i in range(n):
        for j in range(i + 1, n):
            for c in range(k):
                if dna[i][c] != dna[j][c]:
                    unlikeness += 1
    return unlikeness

def print_tree(n):
    """
    Print the tree in the required format.
    Arguments:
        n: number of DNA samples
    """
    for i in range(n - 1):
        print(i, i + 1)

if __name__ == "__main__":
    # Get the input
    f = open(sys.argv[1])
    n, k, dna = get_input(f)

    # Compute the minimal unlikeliness and print it
    unlikeness = min_unlikeness(n, k, dna)
    print(unlikeness)

    # Print the tree
    print_tree(n)
