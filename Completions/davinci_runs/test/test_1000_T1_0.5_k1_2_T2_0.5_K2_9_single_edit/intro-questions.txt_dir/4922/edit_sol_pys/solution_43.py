

def process_input(filename):
    """
    Processes the input file and returns the
    number of clauses (m) and the number of
    variables (n) in the file.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        m, n = lines[0].split()
        return int(m), int(n)

def main():
    """
    Reads the input file, processes it, and prints
    whether it is satisfactory or not.
    """
    m, n = process_input('input/input.txt')

    # if m < 8, it is unsatisfactory
    if m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
