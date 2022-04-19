

def main():
    # Get input
    n, m = [int(x) for x in input().split()]

    # Solve
    print(solve(n, m))

def solve(n, m):
    # Create a set of all possible answers
    answers = set()
    for i in range(n):
        for j in range(m):
            answers.add(i ^ j)

    # Return the number of possible answers
    return len(answers)

if __name__ == '__main__':
    main()
