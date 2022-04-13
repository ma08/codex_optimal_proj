
import sys

def main():
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        M, N, C = line.split()
        M = int(M)
        N = int(N)
        first_matrix = []
        for i in range(M):
            first_matrix.append(sys.stdin.readline())
        sys.stdin.readline()
        second_matrix = []
        for i in range(N):
            second_matrix.append(sys.stdin.readline())
        for i in range(M):
            for j in range(N):
                if second_matrix[i][j] == C:
                    sys.stdout.write(first_matrix[i][j])
                else:
                    sys.stdout.write(second_matrix[i][j])
            sys.stdout.write("\n")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
