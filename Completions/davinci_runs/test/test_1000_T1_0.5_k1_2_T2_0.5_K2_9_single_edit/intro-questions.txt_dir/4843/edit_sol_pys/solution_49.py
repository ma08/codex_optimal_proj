
def check_queens(N, queens):
    for queen in queens:
        x, y = queen
        for queen2 in queens:
            x2, y2 = queen2
            if (x == x2 or y == y2 or abs(x - x2) == abs(y - y2)) and (queen != queen2):
                    return 'INCORRECT'
    return 'CORRECT'

def main():
    N = int(input())
    queens = [list(map(int, input().split())) for i in range(N)]
    print(check_queens(N, queens))

if __name__ == "__main__":
    main()
