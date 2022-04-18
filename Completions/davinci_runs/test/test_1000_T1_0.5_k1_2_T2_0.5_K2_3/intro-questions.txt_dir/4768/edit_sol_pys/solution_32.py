

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

def min_unlikeliness(n, k, dna):
    """
    Compute the minimal unlikeliness of the phylogenetic tree.
    Arguments:
        n: number of DNA samples
        k: length of DNA samples
        dna: list of strings representing the DNA samples
    Returns:
        unlikeliness: the minimal unlikeliness of the phylogenetic tree
    """
    unlikeliness = 0
    for i in range(n):
        for j in range(i + 1, n):
            for c in range(k):
                if dna[i][c] != dna[j][c]:
                    unlikeliness += 1
    return unlikeliness

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
    f = open(sys.argv[1], "r")
    n, k, dna = get_input(f)

    # Compute the minimal unlikeliness and print it
    unlikeliness = min_unlikeliness(n, k, dna)
    print(unlikeliness)

    # Print the tree
    print_tree(n)
