import sys

def is_antisudoku(sudoku):
    for row in sudoku:
        for number in row:
            if row.count(number) < 2:
                return False
    for i in range(9):
        column = [row[i] for row in sudoku]
        for number in column:
            if column.count(number) < 2:
                return False
    for i in range(3):
        for j in range(3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(sudoku[3*i+k][3*j+l])
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
        if is_antisudoku(sudoku):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
