
from itertools import permutations

def solve(problem_list, first_problem_index):
    problem_list.pop(first_problem_index)
    permutations_list = permutations(problem_list)
    num_AC = 0
    penalty_time = 0
    for permutation in permutations_list:
        permutation = list(permutation)
        permutation.insert(0, first_problem_index)
        time_elapsed = 0
        AC_count = 0
        for problem_index in permutation:
            time_elapsed += problem_list[problem_index]
            if time_elapsed > 300:
                break
            AC_count += 1
        if AC_count > num_AC:
            num_AC = AC_count
            penalty_time = time_elapsed
        elif AC_count == num_AC:
            if time_elapsed < penalty_time:
                penalty_time = time_elapsed
    return num_AC, penalty_time

def main():
    N, p = [int(x) for x in input().split()]
    problem_list = [int(x) for x in input().split()]
    num_AC, penalty_time = solve(problem_list, p)
    print(num_AC, penalty_time)

if __name__ == '__main__':
    main()
