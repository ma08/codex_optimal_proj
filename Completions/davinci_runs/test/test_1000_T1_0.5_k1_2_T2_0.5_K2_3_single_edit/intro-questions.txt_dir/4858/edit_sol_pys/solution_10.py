

import sys

def main():
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        M, N, C = line.split()
        M = int(M)
        N = int(N)
        first = []
        for i in range(M):
            first.append(sys.stdin.readline())
        second = []
        sys.stdin.readline()
        for i in range(N):
            second.append(sys.stdin.readline())
        for i in range(M):
            for j in range(N):
                if second[i][j] == C:
                    sys.stdout.write(first[i][j])
                else:
                    sys.stdout.write(second[i][j])
            sys.stdout.write("\n")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
