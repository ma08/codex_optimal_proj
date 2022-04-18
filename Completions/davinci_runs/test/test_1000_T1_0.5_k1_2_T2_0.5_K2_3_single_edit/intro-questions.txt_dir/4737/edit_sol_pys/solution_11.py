

from sys import stdin
from itertools import permutations

N, p = map(int, stdin.readline().split())
est = list(map(int, stdin.readline().split()))  # Time it takes to solve each problem

# If the first problem is estimated to be too long, then we can't solve any problems
if est[p] > 300:
    print(0, 0)
else:
    perms = permutations(range(N))  # Create a list of all the possible permutations of the problems
    perms = sorted(perms, key=lambda x: est[x[0]])  # Sort the list by the time it takes to solve the first problem
    # Find the permutation that solves the most problems
    max_ac = 0
    min_time = 0
    for perm in perms:
        if perm[0] == p:  # If the first problem is the one we want to solve first, then we can start solving it
            time = 0  # Keep track of the time it takes to solve each problem
            ac = 0  # Keep track of how many problems we've solved
            # Try to solve each problem
            for problem in perm:
                if time + est[problem] > 300:  # If we don't have enough time to solve the problem, then we can't solve it
                    break
                else:
                    ac += 1
                    time += est[problem]
            if ac > max_ac:  # If we solved more problems, then update the number of problems solved and the time it took
                max_ac = ac
                min_time = time
    print(max_ac, min_time)
