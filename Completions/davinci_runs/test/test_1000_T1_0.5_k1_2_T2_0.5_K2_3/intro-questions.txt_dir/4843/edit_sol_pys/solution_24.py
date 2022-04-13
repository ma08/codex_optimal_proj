
def main():
    """
    This is the solution to the problem.
    """
    # Read the input
    n = int(input())
    queen = []
    for i in range(n):
        queen.append(tuple(map(int, input().split())))
    # Check if the solution is correct
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if queen[i][0] == queen[j][0] or queen[i][1] == queen[j][1] or abs(queen[i][0] - queen[j][0]) == abs(queen[i][1] - queen[j][1]): # noqa
                correct = False
                break
    # Print the result
    if correct:
        print('CORRECT')
    else:
        print('INCORRECT')

if __name__ == '__main__':
    main()
