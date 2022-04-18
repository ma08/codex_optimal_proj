
def check(queens):
    """
    This function checks if the solution is correct.
    """
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def main():
    """
    This is the solution to the problem.
    """
    # Read the input
    n = int(input())
    queens = []
    for i in range(n):
        queens.append(tuple(map(int, input().split())))
    # Print the result
    if check(queens):
        print('CORRECT')
    else:
        print('INCORRECT')

if __name__ == '__main__':
    main()
