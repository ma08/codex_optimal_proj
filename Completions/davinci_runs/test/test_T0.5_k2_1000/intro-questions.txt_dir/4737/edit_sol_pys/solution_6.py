

from sys import stdin
from itertools import permutations

N, p = map(int, stdin.readline().split())
est = list(map(int, stdin.readline().split()))  # estimated time

# If the first problem is estimated to be too long, then we can't solve any problems
if est[p] > 300:
    print(0, 0)
else:
    # Create a list of all the possible permutations of the problems.
    perms = list(permutations(range(N)))
    # Sort the list by the time it takes to solve the first problem.
    perms = sorted(perms, key=lambda x: est[x[0]])
    # Find the permutation that solves the most problems.
    max_ac = 0
    min_time = 0
    for perm in perms:
        # If the first problem is the one we want to solve first, then we can start solving it.
        if perm[0] == p:
            # Keep track of the time it takes to solve each problem.
            time = 0
            # Keep track of how many problems we've solved.
            ac = 0
            # Try to solve each problem.
            for problem in perm:
                # If we don't have enough time to solve the problem, then we can't solve it.
                if time + est[problem] > 300:
                    break
                # Otherwise, we can solve it.
                else:
                    ac += 1
                    time += est[problem]
            # If we solved more problems, then update the number of problems solved and the time it took.
            if ac > max_ac:
                max_ac = ac
                min_time = time
    print(max_ac, min_time)
