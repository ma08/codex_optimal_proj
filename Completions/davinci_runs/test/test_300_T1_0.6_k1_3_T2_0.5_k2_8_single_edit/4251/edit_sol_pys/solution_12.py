
import sys

class MatrixTraversal:

    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def __str__(self):
        return f"n:{self.n}, m:{self.m}, matrix:{self.matrix}"

    def _print(self):
        print(self)

    def find_max_k(self):
        max_k = 0
        for i in range(self.n):
            for j in range(self.m):
                if i-1 >= 0 and abs(self.matrix[i][j] - self.matrix[i-1][j]) > max_k:
                    max_k = abs(self.matrix[i][j] - self.matrix[i-1][j])
                if i+1 < self.n and abs(self.matrix[i][j] - self.matrix[i+1][j]) > max_k:
                    max_k = abs(self.matrix[i][j] - self.matrix[i+1][j])
                if j-1 >= 0 and abs(self.matrix[i][j] - self.matrix[i][j-1]) > max_k:
                    max_k = abs(self.matrix[i][j] - self.matrix[i][j-1])
                if j+1 < self.m and abs(self.matrix[i][j] - self.matrix[i][j+1]) > max_k:
                    max_k = abs(self.matrix[i][j] - self.matrix[i][j+1])
        return max_k

def main(input_file):
    with open(input_file) as f:
        n, m = f.readline().split(sep=' ')
        matrix = []
        for i in range(int(n)):
            matrix.append([int(x) for x in f.readline().split(sep=' ')])
        matrix_traversal = MatrixTraversal(int(n), int(m), matrix)
        print("max_k:", matrix_traversal.find_max_k())

if __name__ == "__main__":
    main(sys.argv[1])
