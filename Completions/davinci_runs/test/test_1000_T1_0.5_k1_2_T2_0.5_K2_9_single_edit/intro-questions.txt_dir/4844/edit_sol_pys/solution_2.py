

def main():
    # Read input file
    input_file = open("input.txt", "r")
    N = int(input_file.readline())
    M = [list(map(int, line.split())) for line in input_file]

    # Initialize array
    A = [0] * N

    # Process
    for i in range(N):
        for j in range(N):
            if i != j:
                A[i] = M[i][j] | A[j]

    # Write output file
    output_file = open("output.txt", "w")
    output_file.write(' '.join([str(x) for x in A]))

if __name__ == "__main__":
    main()
