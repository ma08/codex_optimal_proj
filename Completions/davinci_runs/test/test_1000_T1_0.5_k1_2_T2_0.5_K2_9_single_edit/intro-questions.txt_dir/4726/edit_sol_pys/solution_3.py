
import math
M, N, T = map(int, input().split())
if T == 1:
    print('AC' if N <= M else 'TLE')
elif T == 2:
    print('AC' if 2 ** N <= M else 'TLE')
elif T == 3:
    print('AC' if N ** 4 <= M else 'TLE')
elif T == 4:
    print('AC' if N ** 3 <= M else 'TLE')
elif T == 5:
    print('AC' if N ** 2 <= M else 'TLE')
elif T == 6:
    print('AC' if N * math.log(N, 2) <= M else 'TLE')
elif T == 7:
    print('AC' if N <= M else 'TLE')
