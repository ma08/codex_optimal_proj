

def solve(seats):
    # Complete this function
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == "o":
                for d in directions:
                    if 0 <= i + d[0] < len(seats) and 0 <= j + d[1] < len(seats[0]):
                        if seats[i + d[0]][j + d[1]] == "o":
                            result += 1
    return result // 2

if __name__ == "__main__":
    R, C = map(int, input().strip().split(' '))
    seats = []
    for _ in range(R):
        seats.append(list(input().strip()))
    result = solve(seats)
    print(result)
