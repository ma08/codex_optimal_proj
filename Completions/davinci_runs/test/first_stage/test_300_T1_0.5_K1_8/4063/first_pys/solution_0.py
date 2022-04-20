

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    problem_count = int(input())
    problem_difficulty = list(map(int, input().split()))
    problem_difficulty.sort()
    half_problem_count = problem_count // 2
    left_sum = sum(problem_difficulty[:half_problem_count])
    right_sum = sum(problem_difficulty[half_problem_count:])
    print(left_sum - right_sum)