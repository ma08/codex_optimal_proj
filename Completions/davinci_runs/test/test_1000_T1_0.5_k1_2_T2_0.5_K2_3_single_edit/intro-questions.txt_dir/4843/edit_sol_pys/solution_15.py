
def check_queens(queens):
    for queen in queens:
        x, y = queen
        for queen2 in queens:
            x2, y2 = queen2
            if x == x2 or y == y2 or abs(x - x2) == abs(y - y2):
                if queen != queen2:
                    return 'INCORRECT'
    return 'CORRECT'

def main():
    queens = [list(map(int, input().split())) for i in range(int(input()))]
    print(check_queens(queens))

if __name__ == "__main__":
    main()
