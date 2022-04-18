

def solve(seats):
    # Complete this function
    R, S = len(seats), len(seats[0])  # number of rows and columns
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    result = 0  # number of pairs of people sitting next to each other
    for i in range(R):
        for j in range(S):
            if seats[i][j] == "o":
                for d in directions:
                    if 0 <= i + d[0] < R and 0 <= j + d[1] < S:
                        if seats[i + d[0]][j + d[1]] == "o":
                            result += 1
    return result // 2

if __name__ == "__main__":
    R, S = map(int, input().strip().split(' '))
    seats = []
    for _ in range(R):
        seats.append(list(input().strip()))
    result = solve(seats)
    print(result)
