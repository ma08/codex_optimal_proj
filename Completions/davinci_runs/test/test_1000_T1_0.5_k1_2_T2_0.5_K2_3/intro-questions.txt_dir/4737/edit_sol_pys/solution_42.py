#!/usr/bin/env python

import sys

def main():
    """
    This function is the main entry point of the program.
    """
    # read input
    N, p = map(int, sys.stdin.readline().split())
    time_estimates = map(int, sys.stdin.readline().split())
    # solve problem
    num_ac, penalty_time = solve_problem(N, p, time_estimates)
    # print output
    print num_ac, penalty_time

def solve_problem(N, p, time_estimates):
    """
    This function solves the problem of finding the optimal number of accepted problems and penalty time
    given the problem set and the problem to solve first.
    """
    # define the number of accepted problems and the penalty time
    num_ac = 0
    penalty_time = 0
    # define the remaining time
    remaining_time = 300
    # define the problem to solve
    problem_to_solve = (p + 1) % N
    # iterate over all problems
    for problem in range(N):
        # check if the problem is the problem to solve
        if problem == problem_to_solve:
            # check if the problem can be solved
            if time_estimates[problem] <= remaining_time:
                # solve the problem
                remaining_time -= time_estimates[problem]
                penalty_time += time_estimates[problem]
                num_ac += 1
                # update the problem to solve
                problem_to_solve = (problem_to_solve + 1) % N
        # check if the problem can be solved
        elif time_estimates[problem] <= remaining_time:
            # solve the problem
            remaining_time -= time_estimates[problem]
            penalty_time += remaining_time
            num_ac += 1
            # update the problem to solve
            problem_to_solve = (problem_to_solve + 1) % N
    return num_ac, penalty_time

if __name__ == "__main__":
    main()
