

def solve(seats):
    # Complete this function
    row_num = len(seats)
    col_num = len(seats[0])
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for i in range(row_num):
        for j in range(col_num):
            if seats[i][j] == 'o':
                for d in direction:
                    if 0 <= i + d[0] < row_num and 0 <= j + d[1] < col_num:
                        if seats[i + d[0]][j + d[1]] == 'o':
                            count += 1
    return count // 2

if __name__ == "__main__":
    row_num, col_num = map(int, input().strip().split(' '))
    seats = []
    for _ in range(row_num):
        seats.append(list(input().strip()))
    result = solve(seats)
    print(result)
