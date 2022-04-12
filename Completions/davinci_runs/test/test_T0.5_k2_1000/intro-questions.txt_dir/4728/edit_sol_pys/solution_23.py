import sys

def parse_molecule(molecule): # parse molecule into a dictionary
    pass

def solve(input_molecule, output_molecule, n): # find the max number of molecules that can be made
    pass

def main():
    input_molecule, n = sys.stdin.readline().split()
    n = int(n)
    output_molecule = sys.stdin.readline().strip()
    print(solve(input_molecule, output_molecule, n))

if __name__ == "__main__":
    main()
