
def main():
    """
    This is the solution to the problem.
    """
    # Read the input
    n = int(input())
    queens = [tuple(map(int, input().split())) for _ in range(n)]
    # Check if the solution is correct
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                correct = False
                break
    # Print the result
    if correct:
        print('CORRECT')
    else:
        print('INCORRECT')

if __name__ == '__main__':
    main()
