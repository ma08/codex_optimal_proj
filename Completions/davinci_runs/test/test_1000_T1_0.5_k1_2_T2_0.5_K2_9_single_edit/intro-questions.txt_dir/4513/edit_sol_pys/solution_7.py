

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
        if is_anti_sudoku(sudoku):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
