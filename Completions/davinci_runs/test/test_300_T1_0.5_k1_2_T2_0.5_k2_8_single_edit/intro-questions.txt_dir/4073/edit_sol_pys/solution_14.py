

def main():
    # Get input and output file names
    input_file = "input.txt"
    output_file = "output.txt"

    # Open the input file
    with open(input_file, "r") as fin:
        # Get input
        n = int(fin.readline())
        a = [int(x) for x in fin.readline().split()]

        # Solve
        ans = solve(n, a)

    # Open the output file
    with open(output_file, "w") as fout:
        # Write the answer
        fout.write(str(ans))

def solve(n, a):
    pass


if __name__ == '__main__':
    main()
