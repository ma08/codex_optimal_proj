

def main():
    """
    1. Read input
    2. Solve problem
    3. Output result
    """
    n, p = map(int, input().split())
    times = list(map(int, input().split()))
    num_ac, penalty_time = solve(n, p, times)
    print("{} {}".format(num_ac, penalty_time))

def solve(n, p, times):
    """
    Solve problem
    """
    first_problem_time = times[p]
    times = times[:p] + times[p + 1:]
    times.sort()
    num_ac = 0
    penalty_time = 0
    while times:
        num_ac += 1
        penalty_time += times[0]
        times = times[1:]
    return num_ac, penalty_time + first_problem_time

    # max_time = 300
    # max_num_ac = 0
    # max_penalty_time = 0
    # for i in range(2**(n-1)):
    #     num_ac = 0
    #     penalty_time = 0
    #     first_problem_time = times[p]
    #     times_left = times[:p] + times[p+1:]
    #     times_left.sort()
    #     for j in range(n-1):
    #         if i & (1 << j):
    #             penalty_time += times_left[j]
    #             times_left[j] = 0
    #     for time in times_left:
    #         if time <= max_time - penalty_time:
    #             max_time -= penalty_time
    #             penalty_time += time
    #             num_ac += 1
    #     penalty_time += first_problem_time
    #     if penalty_time <= max_time:
    #         if num_ac > max_num_ac:
    #             max_num_ac = num_ac
    #             max_penalty_time = penalty_time
    #         elif num_ac == max_num_ac and penalty_time < max_penalty_time:
    #             max_penalty_time = penalty_time
    # return max_num_ac, max_penalty_time

if __name__ == "__main__":
    main()
