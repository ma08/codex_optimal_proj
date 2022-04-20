

import sys

n = int(sys.stdin.readline().rstrip())

digits = [int(x) for x in str(n)]

if digits[-1] == 2 or digits[-1] == 4 or digits[-1] == 5 or digits[-1] == 7 or digits[-1] == 9:
    print("hon")
elif digits[-1] == 0 or digits[-1] == 1 or digits[-1] == 6 or digits[-1] == 8:
    print("pon")
elif digits[-1] == 3:
    print("bon")