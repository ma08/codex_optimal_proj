
from itertools import permutations

def solve(problem_list, first_problem_index):
    #print(problem_list)
    #print(first_problem_index)
    problem_list.pop(first_problem_index)
    permutations_list = list(permutations(problem_list))
    #print(permutations_list)
    num_AC = 0
    penalty_time = 0
    for permutation in permutations_list:
        permutation = list(permutation)
        permutation.insert(0, first_problem_index)
        #print(permutation)
        time_elapsed = 0
        ac_count = 0
        for problem_index in permutation:
            time_elapsed += problem_list[problem_index]
            #print(time_elapsed)
            if time_elapsed > 300:
                break
            ac_count += 1
        #print(ac_count)
        if ac_count > num_AC:
            num_AC = ac_count
            penalty_time = time_elapsed
            #print(penalty_time)
        elif ac_count == num_AC:
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
