

import sys

def main():
    """
    The main function that reads input and calls the other functions
    """
    n = int(sys.stdin.readline())
    string = sys.stdin.readline().rstrip()
    solution = string_sorting(n, string)
    print(len(solution))
    print(*solution)

def string_sorting(n, string):
    """
    Takes the number of characters and the string and returns the solution
    """
    solution = [1]
    for i in range(1, n):
        if string[i] != string[i - 1]:
            solution.append(solution[i - 1] + 1)
        else:
            solution.append(solution[i - 1])
    return solution

if __name__ == "__main__":
    main()