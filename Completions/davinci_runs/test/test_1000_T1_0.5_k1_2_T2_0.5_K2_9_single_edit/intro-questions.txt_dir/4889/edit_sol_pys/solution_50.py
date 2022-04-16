

import sys

def main(n):
    rods = []
    for i in range(n):
        rods.append(i)

    rods.sort()

    while len(rods) > 1:
        rods[0] = rods[0] + rods[1]
        del rods[1]
        rods.sort()

    return rods[0]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(main(n))
