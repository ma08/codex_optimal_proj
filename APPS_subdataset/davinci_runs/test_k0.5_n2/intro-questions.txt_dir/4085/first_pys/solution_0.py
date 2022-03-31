

import math

t = int(input())
for _ in range(t):
    n = int(input())
    divisors = list(map(int, input().split()))

    divisors.sort()

    # print(divisors)

    num_divisors = len(divisors)
    root = math.floor(math.sqrt(divisors[-1]))

    # print(root)

    if root * root == divisors[-1]:
        root -= 1

    # print(root)

    if num_divisors == 1:
        if divisors[0] == 2:
            print(4)
        else:
            print(divisors[0] * 2)
    elif num_divisors == 2:
        if divisors[0] == 2:
            print(divisors[1] * 2)
        else:
            print(divisors[0] * divisors[1])
    else:
        if divisors[0] == 2:
            if divisors[1] == 4:
                print(divisors[-1] * divisors[-2])
            else:
                print(divisors[-1] * 2)
        else:
            print(divisors[-1] * divisors[-2])