
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
    max_num_ac, max_penalty_time = 0, 0
    for i in range(2**(n-1)):
        num_ac = 0
        penalty_time = 0
        times_left = times[:p] + times[p+1:] # Exclude time of the first problem
        times_left.sort() # Sort times from small to large
        for j in range(n-1): # Exclude time of the first problem
            if i & (1 << j): # If j-th bit of i is 1
                penalty_time += times_left[j] # Add the time to the penalty time
                times_left[j] = 0 # Set the time to 0
        for time in times_left: # Check if the remaining problems can be solved
            if time <= 300 - penalty_time: # If the problem can be solved
                penalty_time += time # Add the time to the penalty time
                num_ac += 1 # The number of solved problems increases by one
        penalty_time += times[p] # Add the time of the first problem to the penalty time
        if num_ac > max_num_ac or (num_ac == max_num_ac and penalty_time < max_penalty_time):
            max_num_ac = num_ac
            max_penalty_time = penalty_time
    return max_num_ac, max_penalty_time

if __name__ == "__main__":
    main()
