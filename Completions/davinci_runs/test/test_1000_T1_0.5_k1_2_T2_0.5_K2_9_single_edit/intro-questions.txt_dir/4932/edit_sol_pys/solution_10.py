

import sys

def main():
    line = sys.stdin.readline().split()
    aggr, calm, aggr2, calm2 = [int(n) for n in line]
    line = sys.stdin.readline().split()
    p, m, g = [int(n) for n in line]
    for num in [p, m, g]:
        if (num - 1) % (aggr + calm) < aggr and (num - 1) % (aggr2 + calm2) < aggr2:
            print("both")
        elif (num - 1) % (aggr + calm) < aggr or (num - 1) % (aggr2 + calm2) < aggr2:
            print("one")
        else:
            print("none")

main()
