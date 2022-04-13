
import sys

def is_antisudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i].count(sudoku[i][j]) < 2:
                return False
    for i in range(9):
        for j in range(9):
            if [row[i] for row in sudoku].count(sudoku[j][i]) < 2:
                return False
    for i in range(3):
        for j in range(3):
            block = [sudoku[3*i+k][3*j+l] for k in range(3) for l in range(3)]
            for k in range(3):
                for l in range(3):
                    if block.count(sudoku[3*i+k][3*j+l]) < 2:
                    return False
    return True

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        sudoku = []
        for j in range(9):
            sudoku.append(list(map(int, list(sys.stdin.readline().strip()))))
        if is_antisudoku(sudoku):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
