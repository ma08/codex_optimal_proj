
import math
M, N, T = map(int, input().split())

if T == 1:
    if N > M:
        print("TLE")
    else:
        print("AC")
elif T == 2:
    if 2 ** N > M:
        print("TLE")
    else:
        print("AC")
elif T == 3:
    if N ** 4 > M:
        print("TLE")
    else:
        print("AC")
elif T == 4:
    if N ** 3 > M:
        print("TLE")
    else:
        print("AC")
elif T == 5:
    if N ** 2 > M:
        print("TLE")
    else:
        print("AC")
elif T == 6:
    if N * math.log2(N) > M:
        print("TLE")
    else:
        print("AC")
elif T == 7:
    if N > M:
        print("TLE")
    else:
        print("AC")
