
def main():
    """
    This is the solution to the problem.
    """
    # Read the input
    n = int(input())
    queens = [tuple(map(int, input().split())) for _ in range(n)]
    # Check if the solution is correct.
    correct = all(queens[i][0] != queens[j][0] and queens[i][1] != queens[j][1] and abs(queens[i][0] - queens[j][0]) != abs(queens[i][1] - queens[j][1]) for i in range(n) for j in range(i + 1, n))
    # Print the result
    if correct:
        print('CORRECT')
    else:
        print('INCORRECT')

if __name__ == '__main__':
    main()
