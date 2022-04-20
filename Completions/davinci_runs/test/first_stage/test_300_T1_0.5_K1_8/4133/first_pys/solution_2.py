

import sys
import math

def main():
    # read input
    golorp = sys.stdin.readline().strip()

    # parse input
    golorp = parse(golorp)

    # solve problem
    solution = solve(golorp)

    # print solution
    print(solution)

def parse(golorp):
    """
    Parses the golorp string into a list of operators, variables and parentheses.
    """
    # convert to list of characters
    golorp = list(golorp)

    # replace all operators with their index in the operator list
    operators = ['+', '-', '*', '/']
    for index, operator in enumerate(operators):
        for i in range(0, len(golorp)):
            if golorp[i] == operator:
                golorp[i] = index

    # replace all variables with their index in the variable list
    variables = ['?', ':', '>', '<', '.']
    for index, variable in enumerate(variables):
        for i in range(0, len(golorp)):
            if golorp[i] == variable:
                golorp[i] = index

    # replace all parentheses with their index in the parentheses list
    parentheses = ['(', ')']
    for index, parenthesis in enumerate(parentheses):
        for i in range(0, len(golorp)):
            if golorp[i] == parenthesis:
                golorp[i] = index

    return golorp

def solve(golorp):
    """
    Solves the golorp problem.
    """
    # get the number of variables and operators
    n = len(golorp)
    m = n - 1

    # get the number of possible solutions
    num_solutions = 10**n

    # initialize the solutions
    solutions = [num_solutions * [0] for i in range(0, m)]

    # loop through the number of possible solutions
    for i in range(0, num_solutions):
        # get the solution
        solution = get_solution(i, n)

        # get the result
        result = evaluate(golorp, solution)

        # add the result to the solutions
        if result != -1:
            solutions[result][i] = 1

    # loop through the solutions
    for i in range(0, m):
        # check if the solution is valid
        if all(solution == 1 for solution in solutions[i]):
            # return the solution
            return get_solution(i, n)

    # return false
    return 'false'

def evaluate(golorp, solution):
    """
    Evaluates the golorp expression with the given solution.
    """
    # get the number of variables and operators
    n = len(golorp)
    m = n - 1

    # initialize the stack
    stack = []

    # loop through the characters
    for character in golorp:
        # check if the character is a variable
        if character < 5:
            # push the variable to the stack
            stack.append(solution[character])
        # check if the character is an operator
        elif character < 8:
            # get the operands
            a = stack.pop()
            b = stack.pop()
            c = 0

            # check if the operator is addition
            if character == 5:
                c = (a + b) % 10
            # check if the operator is subtraction
            elif character == 6:
                c = (a - b) % 10
            # check if the operator is multiplication
            elif character == 7:
                c = (a * b) % 10
            # check if the operator is division
            elif character == 8:
                # check if the denominator is 0
                if b == 0:
                    return -1

                # get the quotient
                c = math.floor(a / b)

            # push the result to the stack
            stack.append(c)
        # check if the character is a parenthesis
        elif character < 10:
            # check if the character is an opening parenthesis
            if character == 9:
                # get the next character
                next_character = golorp[golorp.index(character) + 1]

                # check if the next character is a variable
                if next_character < 5:
                    # push the variable to the stack
                    stack.append(solution[next_character])
                # check if the next character is a parenthesis
                elif next_character < 10:
                    # check if the next character is a closing parenthesis
                    if next_character == 10:
                        # pop the result from the stack
                        stack.pop()

    # return the result
    return stack.pop()

def get_solution(i, n):
    """
    Gets the solution for the given index.
    """
    # initialize the solution
    solution = [0 for j in range(0, n)]

    # loop through the solution
    for j in range(0, n):
        # get the value
        value = i % 10

        # set the value in the solution
        solution[j] = value

        # update the index
        i = math.floor(i / 10)

    # return the solution
    return solution

if __name__ == '__main__':
    main()