

import sys

def main():
    R, C = map(int, sys.stdin.readline().split())
    parking_map = []
    for i in range(R):
        parking_map.append(sys.stdin.readline().strip())
    # print(parking_map)
    parking_spaces = [0, 0, 0, 0, 0]  # 0, 1, 2, 3, 4
    for i in range(R):
        for j in range(C):
            # print(i, j)
            if parking_map[i][j] == '.':
                if parking_map[i][j+1] == '.' and parking_map[i+1][j] == '.' and parking_map[i+1][j+1] == '.':
                    parking_spaces[0] += 1
                    if i < R-1 and j < C-1:
                        if parking_map[i][j+2] == 'X':
                            parking_spaces[1] += 1
                        if parking_map[i+2][j] == 'X':
                            parking_spaces[1] += 1
                        if parking_map[i+2][j+1] == 'X':
                            parking_spaces[1] += 1
                        if parking_map[i+1][j+2] == 'X':
                            parking_spaces[1] += 1
                    if i < R-2 and j < C-2:
                        if parking_map[i+2][j+2] == 'X':
                            parking_spaces[2] += 1
                        if parking_map[i+3][j+1] == 'X':
                            parking_spaces[2] += 1
                        if parking_map[i+1][j+3] == 'X':
                            parking_spaces[2] += 1
                    if i < R-3 and j < C-3:
                        if parking_map[i+3][j+2] == 'X':
                            parking_spaces[3] += 1
                        if parking_map[i+2][j+3] == 'X':
                            parking_spaces[3] += 1
                    if i < R-4 and j < C-4:
                        if parking_map[i+3][j+3] == 'X':
                            parking_spaces[4] += 1
    for i in range(5):
        print(parking_spaces[i])

if __name__ == '__main__':
    main()
