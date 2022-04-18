

from sys import stdin
from itertools import permutations

N, p = map(int, stdin.readline().split())
est = list(map(int, stdin.readline().split()))

if est[p] > 300:
    print(0, 0)
else:
    perms = permutations(range(N))
    perms = sorted(perms, key=lambda x: est[x[0]])
    max_ac = 0
    min_time = 0
    for perm in perms:
        if perm[0] == p:
            time = 0
            ac = 0
            for problem in perm:
                if time + est[problem] > 300:
                    break
                else:
                    ac += 1
                    time += est[problem]
            if ac > max_ac:
                max_ac = ac
                min_time = time
    print(max_ac, min_time)
