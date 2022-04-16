

import sys

def is_anti_sudoku(sudoku):
    for row in sudoku:
        for number in row:
            if row.count(number) < 2:
                return False
    for i in range(9):
        column = [row[i] for row in sudoku]
        for number in column:
            if column.count(number) < 2:
                return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = sudoku[i][j:j+3] + sudoku[i+1][j:j+3] + sudoku[i+2][j:j+3]
            for number in block: 
                if block.count(number) < 2: 
                    return False 
    return True

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        sudoku = []
        for j in range(9):
            sudoku.append(list(map(int, list(sys.stdin.readline().strip()))))
        if is_anti_sudoku(sudoku):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
