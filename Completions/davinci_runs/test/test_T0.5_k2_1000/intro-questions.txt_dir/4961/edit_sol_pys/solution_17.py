

def solve(seats, R, S):
    # Complete this function
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 8 directions
    result = 0
    for i in range(R):
        for j in range(S):
            if seats[i][j] == "o":  # if there is a person
                for d in directions:
                    if 0 <= i + d[0] < R and 0 <= j + d[1] < S:  # if the direction is valid
                        if seats[i + d[0]][j + d[1]] == "o":  # if there is a person
                            result += 1
    return result // 2

if __name__ == "__main__":
    R, S = map(int, input().strip().split(' '))
    seats = []
    for _ in range(R):
        seats.append(list(input().strip()))
    result = solve(seats, R, S)
    print(result)
