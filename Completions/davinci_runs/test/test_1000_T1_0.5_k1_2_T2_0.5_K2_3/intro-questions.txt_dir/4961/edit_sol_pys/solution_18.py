
def solve(seats):
    # Complete this function
    r, s = len(seats), len(seats[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0
    for i in range(r):
        for j in range(s):
            if seats[i][j] == "o":
                for d in directions:
                    if 0 <= i + d[0] < r and 0 <= j + d[1] < s:
                        if seats[i + d[0]][j + d[1]] == "o":
                            result += 1
    return result // 2

if __name__ == "__main__":
    r, s = map(int, input().strip().split(' '))
    seats = []
    for _ in range(r):
        seats.append(list(input().strip()))
    result = solve(seats)
    print(result)
